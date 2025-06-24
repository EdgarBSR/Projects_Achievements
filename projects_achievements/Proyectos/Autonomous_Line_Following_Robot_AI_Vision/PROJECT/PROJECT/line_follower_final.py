
import rclpy
from rclpy.node import Node
import cv2
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
from std_msgs.msg import String

class LineFollower(Node):
    def __init__(self):
        super().__init__('line_follower')
        
        # CAP_DSHOW 
        # Parámetros para detección de línea
        self.colorLower = np.array([0, 0, 0])
        self.colorUpper = np.array([180, 255, 80])
        
        # Parámetros PID optimizados
        '''
        self.Kp = 0.03 o 0.015
        self.Ki = 0.001
        self.Kd = 0.01
        '''
        self.Kp = 0.01
        self.Ki = 0.0
        self.Kd = 0.009
        self.integral = 0.0
        self.previous_error = 0.0
        self.previous_angular_velocity = 0.0
        self.smoothing_factor = 0.4
        self.max_angular_speed = 0.5
        
        # Buffer para filtrado
        self.error_buffer = []
        self.buffer_size = 3
        
        # Parámetros de seguimiento
        self.base_linear_speed = 0.125
        self.min_contour_area = 50
        self.anticipation_factor = 0.3
        
        # Procesamiento de imagen
        self.bridge = CvBridge()
        self.image_center_x = 0
        self.image_received = False
        self.cv_img = None
        
        # Publishers y subscribers
        self.create_subscription(String, "state_light", self.state_light, 10) 
        self.create_subscription(String, "state_signal", self.state_signal, 10) 
        self.create_subscription(String, "state_crossing", self.state_crossing, 10) 
        self.image_sub = self.create_subscription(Image, '/video_source/raw', self.camera_callback, 10)
        self.create_subscription(String, "crossing_status", self.crossing_status_callback, 10)
        self.processed_img_pub = self.create_publisher(Image, '/line_following', 10)
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.crossing = self.create_publisher(String, '/crossing', 10)

        self.message_light = ''
        self.flag_light = False
        self.message_signal = ''
        self.flag_signal = False
        self.message_crossing= ''
        self.flag_crossing = True
        self.timer = self.create_timer(0.01, self.control_loop)
        
        self.type = None
        self.signal_timer_start = None
        self.signal_timer_active = False
        self.time_clock = 0
        
        # Variable para evitar repetir acciones de señales
        self.previous_message = None
        
        self.C = 0.0
        self.get_logger().info('Line follower node started - RACING MODE')

    # Callback para recibir estado del cruce desde points_cross
    def crossing_status_callback(self, data):
        status = data.data
        
        if status == "crossing_started":
            self.flag_crossing = False  # Pausar seguimiento de línea
            self.get_logger().info('🛑 Line following PAUSED - Crossing in progress...')
            
        elif status == "crossing_complete":
            self.flag_crossing = True   # Reactivar seguimiento de línea
            self.get_logger().info('🟢 Line following RESUMED - Crossing completed!')
    
    def state_light(self, data):
        self.message_light = data.data
        self.flag_light = True

    def state_signal(self, data): 
        self.message_signal = data.data
        self.flag_signal= True

    def state_crossing(self, data): 
        self.message_crossing = data.data
        
        # Solo log para debug:
        if self.message_crossing == "crossing":
            self.get_logger().info('🔍 Crossing detected by vision system')
    

    def camera_callback(self, msg):
        try:
            # Convertir mensaje ROS a formato OpenCV
            cv_img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            cv_img = cv2.rotate(cv_img, cv2.ROTATE_180)
            
            self.cv_img = cv_img
            
            # Establecer el centro de la imagen solo una vez
            if not self.image_received:
                image = self.cv_img.copy()
                height, width = image.shape[:2]
                roi_height = int(height * 0.4)
                roi_y = height - roi_height
                roi = image[roi_y:height, 15:width-15]

                self.image_center_x = roi.shape[1]// 2

                self.get_logger().info(f'Image received. Resolution: {self.cv_img.shape[1]}x{self.cv_img.shape[0]}')
                self.get_logger().info(f'Image center at x={self.image_center_x}')

            self.image_received = True

        except Exception as e:
            self.get_logger().error(f'Failed to process image: {str(e)}')

    def detect_line(self):
        if not self.image_received or self.cv_img is None:
            return None, 0, False, 0.0

        image = self.cv_img.copy()
        height, width = image.shape[:2]

        # Región inferior (ROI)
        roi_height = int(height * 0.4)
        roi_y = height - roi_height
        roi = image[roi_y:height, 15:width-15]

        # Conversión a HSV y desenfoque
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        hsv = cv2.GaussianBlur(hsv, (3, 3), 0)

        # Escala de grises para umbral adaptativo
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

        _, thresh = cv2.threshold(gray,100, 255, cv2.THRESH_BINARY_INV)
        #thresh = cv2.adaptiveThreshold(
        #    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
        #    cv2.THRESH_BINARY_INV, 11, 3
        #)

        # Máscara HSV para línea negra
        mask = cv2.inRange(hsv, self.colorLower, self.colorUpper)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=4)

        # Combinación con umbral
        combined_mask = cv2.bitwise_and(mask, thresh)

        # Resultado para visualización
        result = cv2.bitwise_and(roi, roi, mask=combined_mask)
        debug_mask = result.copy()
        # Find contours
        contours, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                
        line_detected = False
        curvature = 0.0
        debug_mask = result.copy()
        line_x = self.image_center_x
        combined_img = roi.copy()
        if contours:
            # Encontrar el contorno más grande (asumiendo que es la línea)
            valid_contours = [c for c in contours if cv2.contourArea(c) > self.min_contour_area]
            if valid_contours:
                largest_contour = max(valid_contours, key=cv2.contourArea)
                # Obtener los momentos del contorno
                M = cv2.moments(largest_contour)
                # Calcular el centroide del contorno
                if M["m00"] != 0:
                    line_x = int(M["m10"] / M["m00"])
                    line_y = int(M["m01"] / M["m00"])
                    line_detected = True
                    # Ajustar line_x a las coordenadas de la imagen completa
                    # Dibujar el contorno y centroide para visualización
                    cv2.drawContours(debug_mask, [largest_contour], -1, (0, 255, 0), 1)
                    cv2.circle(debug_mask, (line_x, line_y), 2, (0, 0, 255), -1)
                    # Visualizar en la imagen original también
                    cv2.drawContours(roi, [largest_contour], -1, (0, 255, 0), 1)
                    cv2.circle(roi, (line_x, line_y), 2, (0, 0, 255), -1)
        
            # Dibujar línea de referencia del centro
            cv2.line(debug_mask, (self.image_center_x, 0), 
                    (self.image_center_x, debug_mask.shape[0]), (255, 0, 0), 1)
            
            cv2.line(roi, (roi.shape[1]// 2, 0), 
                    (roi.shape[1]// 2, roi.shape[0]), (255, 0, 0), 1)
            
            # Dibujar límite del ROI en la imagen original
            cv2.line(image, (0, roi_y), (width, roi_y), (255, 0, 0), 1)
            # Copia de la ROI procesada en la imagen original
            image[roi_y:height, 15:width-15] = roi.copy()
            combined_img = roi.copy()
            
    
            if contours and valid_contours and M["m00"] != 0:
                
                return combined_img, line_x, True, curvature

            


    def control_loop(self):
        
        if self.flag_crossing:
            processed_img, line_x, line_detected, curvature = self.detect_line()
            
            try:
                self.processed_img_pub.publish(self.bridge.cv2_to_imgmsg(processed_img, "bgr8"))
            
            except Exception as e:
                self.get_logger().error(f'Command publish error: {str(e)}')

            current_time = self.get_clock().now().seconds_nanoseconds()[0]

            # Detecta nueva señal o cambio de mensaje
            if self.flag_signal and line_detected:
                if not self.signal_timer_active or self.message_signal != self.previous_message:
                    if self.message_signal == 'GiveWay':
                        self.base_linear_speed = 0.08
                        self.time_clock = 10
                        self.signal_timer_active = True
                        self.signal_timer_start = current_time
                        self.previous_message = self.message_signal  # Guarda mensaje anterior
                        self.Kp = 0.01

                    elif self.message_signal == 'Stop':
                        self.base_linear_speed = 0.0
                        self.time_clock = 10
                        self.signal_timer_active = True
                        self.signal_timer_start = current_time
                        self.previous_message = self.message_signal  # Guarda mensaje anterior
                        self.Kp = 0.0

                    elif self.message_signal == 'Work':
                        self.base_linear_speed = 0.04
                        self.time_clock = 5
                        self.signal_timer_active = True
                        self.signal_timer_start = current_time
                        self.previous_message = self.message_signal  # Guarda mensaje anterior
                        self.Kp = 0.01

                    # Manejo de otras señales
                    elif self.message_signal == 'Forward':
                        self.get_logger().info('Forward signal detected - maintaining speed')
                        direction_msg = String()
                        direction_msg.data = 'straight'
                        self.crossing.publish(direction_msg)  # ✅ AHORA SÍ PUBLICA

                    elif self.message_signal == 'Left':
                        self.get_logger().info('Left signal detected')
                        direction_msg = String()
                        direction_msg.data = 'left'
                        self.crossing.publish(direction_msg)  # ✅ AHORA SÍ PUBLICA

                    elif self.message_signal == 'Right':
                        self.get_logger().info('Right signal detected')
                        direction_msg = String()
                        direction_msg.data = 'right'
                        self.crossing.publish(direction_msg)  # ✅ AHORA SÍ PUBLICA

            # Si el temporizador está activo, evalúa si ya terminó
            if self.signal_timer_active:
                elapsed = current_time - self.signal_timer_start
                if elapsed >= self.time_clock:
                    self.signal_timer_active = False
                    self.base_linear_speed = 0.125  # Velocidad base del segundo set

            # Si no hay señal ni temporizador, asegurar la  velocidad base y limpieza
            if not self.flag_signal and not self.signal_timer_active:
                self.base_linear_speed = 0.125  # Velocidad base del segundo set
                self.previous_message = None
                    
                
            twist_msg = Twist()
            if line_detected:
                # 1. CALCULAR ERROR
                error = self.image_center_x - line_x
                advanced_error = error * (1 + self.anticipation_factor * abs(curvature))
                
                self.error_buffer.append(advanced_error)
                if len(self.error_buffer) > self.buffer_size:
                    self.error_buffer.pop(0)
                filtered_error = float(sum(self.error_buffer) / len(self.error_buffer))
                
                 # 2. ALGORITMO PID
                self.integral += filtered_error
                self.integral = max(min(self.integral, 1000), -1000)
                
                derivative = filtered_error - self.previous_error
                
                angular_velocity = (self.Kp * filtered_error) + (self.Ki * self.integral) + (self.Kd * derivative)
                angular_velocity = (self.smoothing_factor * angular_velocity) + \
                                ((1 - self.smoothing_factor) * self.previous_angular_velocity)
                angular_velocity = max(min(float(angular_velocity), self.max_angular_speed), -self.max_angular_speed)
                
                 # 3. AJUSTE DE VELOCIDAD SEGÚN CURVATURA
                error_ratio = abs(filtered_error) / self.image_center_x
                angular_ratio = abs(angular_velocity) / self.max_angular_speed
                speed_reduction = max(error_ratio, angular_ratio)**2
                
                adjusted_linear_speed = float(self.base_linear_speed * (1 - speed_reduction))
                adjusted_linear_speed = max(adjusted_linear_speed, float(self.base_linear_speed * 0.4))
                
                if abs(filtered_error) > self.image_center_x * 0.4:
                    self.integral = 0.0
                    
             # 4. ENVIAR COMANDOS AL ROBOT
                # Conversión explícita a float nativo
                twist_msg.linear.x = float(adjusted_linear_speed)
                twist_msg.angular.z = float(angular_velocity)
                
                self.previous_error = filtered_error
                self.previous_angular_velocity = angular_velocity
                
                self.get_logger().info(f'Tracking: X={line_x}, Vel={adjusted_linear_speed:.2f}, Ang={angular_velocity:.2f}')
            
            else:
                twist_msg.linear.x = 0.0
                twist_msg.angular.z = 0.0
                #twist_msg.angular.z = 0.0
                self.get_logger().warning('Line lost! Searching...')

            self.cmd_vel_pub.publish(twist_msg)
            self.flag_light = False
            

def main(args=None):
    rclpy.init(args=args)
    line_follower = LineFollower()
    
    try:
        rclpy.spin(line_follower)
    except KeyboardInterrupt:
        pass
    finally:
        stop_msg = Twist()
        stop_msg.linear.x = 0.0
        stop_msg.angular.z = 0.0
        for _ in range(5):
            line_follower.cmd_vel_pub.publish(stop_msg)
            rclpy.spin_once(line_follower, timeout_sec=0.1)
        
        line_follower.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()


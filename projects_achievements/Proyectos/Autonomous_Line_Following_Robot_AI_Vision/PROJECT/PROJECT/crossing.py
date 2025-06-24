
import rclpy
from rclpy.node import Node
import cv2
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from std_msgs.msg import String
import cv2

 
class CV(Node):
    def __init__(self):
        super().__init__('CROSS')

        self.bridge = CvBridge()
        self.msg = String()
        # SUSCRIPTOR: Recibe video de la cámara
        self.sub = self.create_subscription(Image, '/video_source/raw', self.camera_callback, 10)
        # PUBLICADORES
        self.pub = self.create_publisher(Image, 'crossing', 10)
        self.state = self.create_publisher(String, '/state_crossing', 10)
        # Control de imágenes recibidas
        self.image_received_flag = False 
        dt = 0.05
        self.timer = self.create_timer(dt, self.timer_callback)
        self.get_logger().info('CROSS Node started')
        # ============= VARIABLES DE DETECCIÓN =============
        self.message = ''
        self.msg.data = self.message
        self.state.publish(self.msg)
        self.cont = 0

    def camera_callback(self, msg):
        try: 
            # Convertir imagen de ROS (sensor_msgs/Image) a formato OpenCV (matriz numpy)
            # bgr8 = formato de color azul-verde-rojo con 8 bits por canal
            self.cv_img= self.bridge.imgmsg_to_cv2(msg, "bgr8") 
            self.cv_img = cv2.rotate(self.cv_img, cv2.ROTATE_180)
            self.image_received_flag = True 
            
        except:
            self.get_logger().info('Failed to get an image')
 
 
    def timer_callback(self):
        self.cont = 0 
        if self.image_received_flag:
            self.image_received_flag = False
            frame = self.cv_img.copy()
            height, width = frame.shape[:2]

            # Región inferior (ROI)
            roi_height = int(height * 0.30)
            roi_y = height - roi_height
            roi = frame[20-roi_y:height, 20:width-20]
            # Convertir a escala de grises y suavizar
            gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)

            # Aumentar contraste con CLAHE
            clahe = cv2.createCLAHE(clipLimit=4.0)
            gray_eq = clahe.apply(blurred)

            # Umbral binario inverso
            _, binary = cv2.threshold(gray_eq, 100, 255, cv2.THRESH_BINARY_INV)

            # Cierre morfológico
            kernel = np.ones((3, 3), np.uint8)
            closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

            # Detección de contornos
            contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            # ============= ANÁLISIS DE FORMAS =============
            for cnt in contours:
                approx = cv2.approxPolyDP(cnt, 0.1 * cv2.arcLength(cnt, True), True)
                area = cv2.contourArea(cnt)
            # ============= CRITERIOS PARA DETECTAR CRUCE =============
                if len(approx) == 4 and area > 100 and area <250 and cv2.isContourConvex(approx):
                    cv2.drawContours(roi, [approx], -1, (0, 255, 0), 1) 
                    self.cont +=1 

            # ============= DECISIÓN FINAL =============
            if self.cont >= 3:
                self.message = 'crossing'
                self.msg.data = self.message
                self.state.publish(self.msg)
                self.get_logger().info('CROSSING')
        
            self.pub.publish(self.bridge.cv2_to_imgmsg(roi ,'bgr8'))
            
     
def main(args=None):
    rclpy.init(args=args)
    cv_e = CV()
    rclpy.spin(cv_e)
    cv_e.destroy_node()
    rclpy.shutdown()
 
if __name__ == '__main__':
    main()
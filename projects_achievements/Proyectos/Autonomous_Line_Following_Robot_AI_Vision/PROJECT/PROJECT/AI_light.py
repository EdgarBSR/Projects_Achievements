import rclpy
from rclpy.node import Node
import cv2
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from std_msgs.msg import String
import cv2
from ultralytics import YOLO
 
class CV(Node):
    def __init__(self):
        super().__init__('AI')

        self.bridge = CvBridge()
        self.msg = String()
        # Subscribers
        self.sub = self.create_subscription(Image, '/video_source/raw', self.camera_callback, 10)
        # Publishers
        self.pub = self.create_publisher(Image, 'AI_light', 10)
        self.state = self.create_publisher(String, 'state_light', 10)
        # Bandera para saber si ya recibimos una imagen
        self.image_received_flag = False 
        dt = 0.05
        self.timer = self.create_timer(dt, self.timer_callback)
        self.get_logger().info('AI Node started')
        self.model = YOLO("/home/rony/ros2_ws/src/PROJECT/PROJECT/models/bestv03.pt")
        #self.model = YOLO("/home/rony/ros2_ws/src/PROJECT/PROJECT/models/best06.pt")

        # ============= INICIALIZACIÓN DE VARIABLES =============
        self.message = ''
        self.msg.data = self.message
        self.state.publish(self.msg)

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
        """
        FUNCIÓN PRINCIPAL: Se ejecuta cada 0.01 segundos para procesar imágenes
        PROPÓSITO: Detectar semáforos usando inteligencia artificial
        """
        if self.image_received_flag:
            self.image_received_flag = False
            try:
                results = self.model(source=self.cv_img, conf=0.3, verbose = False)
                boxes = results[0].boxes
                ids = boxes.cls.int().tolist()
                 # ============= INTERPRETAR RESULTADOS =============
                if ids:
                    first_id = ids[0]
                    # MAPEO DE IDs A COLORES:
                    # 0 = verde, 1 = rojo, 2 = amarillo
                    self.message = {0: 'green', 1: 'red', 2: 'yellow'}.get(first_id, 'yellow')
                else:
                    self.message = ''
                 # ============= PUBLICAR RESULTADOS =============
                annotated_frame = results[0].plot()
                self.pub.publish(self.bridge.cv2_to_imgmsg(annotated_frame, 'bgr8'))
                self.msg.data = self.message
                self.state.publish(self.msg)
    
            except Exception as e:
                self.get_logger().error(f'Detection error: {e}')
     
def main(args=None):
    rclpy.init(args=args)
    cv_e = CV()
    rclpy.spin(cv_e)
    cv_e.destroy_node()
    rclpy.shutdown()
 
if __name__ == '__main__':
    main()
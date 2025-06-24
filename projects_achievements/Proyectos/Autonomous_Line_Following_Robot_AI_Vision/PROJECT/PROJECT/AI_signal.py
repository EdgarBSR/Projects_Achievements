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
        super().__init__('AI2')

        self.bridge = CvBridge()
        self.msg = String()
        self.sub = self.create_subscription(Image, '/video_source/raw', self.camera_callback, 10)
        self.pub = self.create_publisher(Image, 'AI_signal', 10)
        self.state = self.create_publisher(String, 'state_signal', 10)
        
        self.image_received_flag = False #This flag is to ensure we received at least one image 
        dt = 0.01
        self.timer = self.create_timer(dt, self.timer_callback)
        self.get_logger().info('AI Node started')
        self.model = YOLO("/home/rony/ros2_ws/src/PROJECT/PROJECT/models/best_1_signal.pt")
        self.message = ''
        self.msg.data = self.message
        self.state.publish(self.msg)

    def camera_callback(self, msg):
        try: 
            # We select bgr8 because its the OpenCV encoding by default 
            self.cv_img= self.bridge.imgmsg_to_cv2(msg, "bgr8") 
            self.cv_img = cv2.rotate(self.cv_img, cv2.ROTATE_180)
            self.image_received_flag = True 
            
        except:
            self.get_logger().info('Failed to get an image')
 
 
    def timer_callback(self):
        if self.image_received_flag:
            self.image_received_flag = False
            try:
                results = self.model(source=self.cv_img, conf=0.73,verbose = False)
                boxes = results[0].boxes
                ids = boxes.cls.int().tolist()

                if ids:
                    first_id = ids[0]
                    self.message = {0: 'GiveWay', 1: 'Stop', 2: 'Forward', 3: 'Left', 4: 'Right', 5: 'Work'}.get(first_id)
                else:
                    self.message = ''

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
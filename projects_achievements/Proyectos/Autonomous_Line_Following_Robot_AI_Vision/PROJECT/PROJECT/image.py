import rclpy
from rclpy.node import Node
import cv2
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2
from ultralytics import YOLO
import keyboard 
import os 
from datetime import datetime
import time
class CVimage(Node):
    def __init__(self):
        super().__init__('IMAGE')

        self.bridge = CvBridge()
 
        self.sub = self.create_subscription(Image, '/video_source/raw', self.camera_callback, 10)
        self.pub = self.create_publisher(Image, 'photo', 10)
        
        self.image_received_flag = False #This flag is to ensure we received at least one image 
        dt = 0.1
        self.timer = self.create_timer(dt, self.timer_callback)
        #self.timer2 = self.create_timer(dt, self.timer_callback2)
        self.get_logger().info('ros_color_tracker Node started')
        self.model = YOLO("/home/kokas/Desktop/ROS2/src/PROJECT/PROJECT/best.pt")
        self.a = 0

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
            self.image_received_flag=False
            frame = self.cv_img
    
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            image_path = os.path.join(os.path.expanduser("~"), "images", f"image_{timestamp}.jpg")
            
            # Save the image
            os.makedirs("/home/images", exist_ok=True)
            c=cv2.imwrite(image_path, frame)
            print(c)
            print(f"Image saved at {image_path}")
            self.pub.publish(self.bridge.cv2_to_imgmsg(frame ,'bgr8'))
            
            time.sleep(5)


     
def main(args=None):
    rclpy.init(args=args)
    cv_e = CVimage()
    rclpy.spin(cv_e)
    cv_e.destroy_node()
    rclpy.shutdown()
 
if __name__ == '__main__':
    main()
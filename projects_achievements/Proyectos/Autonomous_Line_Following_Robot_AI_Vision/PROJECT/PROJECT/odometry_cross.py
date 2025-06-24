import rclpy 
from rclpy.node import Node 
from geometry_msgs.msg import Pose2D, Twist
from std_msgs.msg import Float32, Bool, String
from rclpy import qos 
import numpy as np 
import math

class OdometryCross(Node):  
    def __init__(self):  
        super().__init__('odometry_cross') 
        
        ###########  INIT PUBLISHERS ################ 
        self.pub_pose = self.create_publisher(Pose2D, 'pose', 10)
        self.pub_cmd_vel = self.create_publisher(Twist, 'cmd_vel', 10)
        self.pub_movement_complete = self.create_publisher(Bool, 'movement_complete', 10)
        self.pub_rotation_complete = self.create_publisher(Bool, 'rotation_complete', 10)
        
        ############## SUBSCRIBERS ##################  
        self.create_subscription(Float32, "VelocityEncR", self.wr_cb, qos.qos_profile_sensor_data)  
        self.create_subscription(Float32, "VelocityEncL", self.wl_cb, qos.qos_profile_sensor_data)
        self.create_subscription(Float32, "move_distance", self.move_distance_cb, 10)
        self.create_subscription(Float32, "rotate_angle", self.rotate_angle_cb, 10)
        self.create_subscription(String, "state_light", self.state_light, 10) 
        
        ############ ROBOT CONSTANTS ################  
        self.r = 0.05  # wheel radius [m] 
        self.L = 0.19  # wheel separation [m] 
        self.wl = 0.0  # Left wheel speed [rad/s] 
        self.wr = 0.0  # Right wheel speed [rad/s] 
        self.x = 0.1   # Robot position in x-axis [m] 
        self.y = 0.0   # Robot position in y-axis [m] 
        self.theta = 0.0  # Robot orientation [rad] 
        self.robot_pose = Pose2D()
        self.prev_time_ns = self.get_clock().now().nanoseconds
        
        ############ MOVEMENT CONTROL ################
        # Estados de movimiento
        self.is_moving = False
        self.is_rotating = False
        
        # Control de movimiento lineal
        self.target_distance = 0.1
        self.start_x = 0.0
        self.start_y = 0.0
        self.movement_speed = 0.125  # Velocidad lineal [m/s]
        self.distance_tolerance = 0.01  # Tolerancia de distancia [m]
        
        # Control de rotación
        self.target_angle = 0.0
        self.start_theta = 0.0
        self.rotation_speed = 0.3  # Velocidad angular [rad/s]
        self.angle_tolerance = 0.02  # Tolerancia angular [rad] (~1 grado)
        
        timer_period = 0.05 
        self.create_timer(timer_period, self.main_timer_cb) 
        self.get_logger().info("Odometry Cross node initialized!") 

        self.message_light = ''
        self.flag_light = False
        self.current_traffic_light = None

        # ==================== FUNCIONES DE SEMÁFORO ====================

    def state_light(self, data):
        # ACTIVADO: Callback para recibir estados de semáforos
        self.message_light = data.data
        
        # 🚦 ACTUALIZAR ESTADO PERSISTENTE solo si hay cambio
        if self.message_light and self.message_light != self.current_traffic_light:
            self.current_traffic_light = self.message_light
            self.flag_light = True  # Marcar que hubo cambio
            self.get_logger().info(f'🚦 Traffic light CHANGED to: {self.current_traffic_light}')
        elif self.message_light:
            # Mismo color, no marcar cambio pero mantener detección
            self.get_logger().debug(f'🚦 Traffic light maintained: {self.current_traffic_light}')

    def main_timer_cb(self): 
        v, w = self.get_robot_velocity(self.wl, self.wr)
        self.update_robot_pose(v, w)
        
        # Publicar la pose
        self.pub_pose.publish(self.robot_pose)
        
        # Control de movimiento o rotación
        if self.is_moving:
            self.control_movement()
        elif self.is_rotating:
            self.control_rotation()

    def wl_cb(self, wl):  
        self.wl = wl.data 

    def wr_cb(self, wr):  
        self.wr = wr.data
        
    def move_distance_cb(self, msg):
        """Callback para recibir comandos de movimiento lineal"""
        if not self.is_moving and not self.is_rotating:
            self.target_distance = msg.data
            self.start_linear_movement()
        else:
            self.get_logger().warn("Already moving/rotating, ignoring new movement command")
    
    def rotate_angle_cb(self, msg):
        """Callback para recibir comandos de rotación"""
        if not self.is_moving and not self.is_rotating:
            self.target_angle = msg.data
            self.start_rotation()
        else:
            self.get_logger().warn("Already moving/rotating, ignoring new rotation command")
    
    def start_linear_movement(self):
        """Inicia un movimiento lineal"""
        self.is_moving = True
        self.start_x = self.x
        self.start_y = self.y
        self.get_logger().info(f"Starting linear movement: {self.target_distance:.3f}m")
        
    def start_rotation(self):
        """Inicia una rotación"""
        self.is_rotating = True
        self.start_theta = self.theta
        direction = "right" if self.target_angle < 0 else "left"
        self.get_logger().info(f"Starting rotation: {math.degrees(abs(self.target_angle)):.1f}° to the {direction}")
        
    def control_movement(self):
         # 🚦 CONTROL PERSISTENTE DE SEMÁFOROS (siempre activo)
        if self.current_traffic_light == 'green':
            # Si había estado en rojo/amarillo, restaurar velocidad normal
            if self.flag_light:
                self.movement_speed = 0.125
                self.get_logger().info('🟢 GREEN light - Normal speed RESUMED')
                self.flag_light = False

        elif self.current_traffic_light == 'yellow':
            # Si había cambio, actualizar a velocidad reducida
            if self.flag_light:
                self.movement_speed= 0.02
                self.get_logger().info('🟡 YELLOW light - Reduced speed')
                self.flag_light = False

        elif self.current_traffic_light == 'red':
            # Si había cambio, detener completamente
            if self.flag_light:
                self.movement_speed = 0.0
                self.get_logger().info('🔴 RED light - STOPPED (waiting for GREEN)')
                self.flag_light = False
            # MANTENER DETENIDO hasta que cambie a verde
            self.base_linear_speed = 0.0

        
        """Controla el movimiento lineal"""
        distance_traveled = math.sqrt((self.x - self.start_x)**2 + (self.y - self.start_y)**2)
        
        cmd_vel = Twist()
        
        if distance_traveled >= (self.target_distance - self.distance_tolerance):
            # Movimiento completado
            cmd_vel.linear.x = 0.0
            cmd_vel.angular.z = 0.0
            self.is_moving = False
            
            # Notificar completado
            complete_msg = Bool()
            complete_msg.data = True
            self.pub_movement_complete.publish(complete_msg)
            
            self.get_logger().info(f"Linear movement completed! Distance: {distance_traveled:.3f}m")
        else:
            # Continuar movimiento con velocidad constante
            cmd_vel.linear.x = self.movement_speed
            cmd_vel.angular.z = 0.0
            
            if int(distance_traveled * 100) % 5 == 0:  # Log cada 5cm
                self.get_logger().info(f"Moving: {distance_traveled:.3f}m / {self.target_distance:.3f}m")
        
        self.pub_cmd_vel.publish(cmd_vel)
        
    def control_rotation(self):
        cmd_vel = Twist()


        """Controla la rotación"""
        # Calcular ángulo rotado considerando el wrap-around
        angle_rotated = self.theta - self.start_theta
        
        # Normalizar el ángulo a [-pi, pi]
        while angle_rotated > math.pi:
            angle_rotated -= 2 * math.pi
        while angle_rotated < -math.pi:
            angle_rotated += 2 * math.pi
            
        
        if abs(angle_rotated - self.target_angle) <= self.angle_tolerance:
            # Rotación completada
            cmd_vel.linear.x = 0.0
            cmd_vel.angular.z = 0.0
            self.is_rotating = False
            
            # Notificar completado
            complete_msg = Bool()
            complete_msg.data = True
            self.pub_rotation_complete.publish(complete_msg)
            
            self.get_logger().info(f"Rotation completed! Angle: {math.degrees(angle_rotated):.1f}°")
        else:
            # Continuar rotación con velocidad constante
            remaining_angle = self.target_angle - angle_rotated
            
            # Determinar dirección y aplicar velocidad constante
            if remaining_angle > 0:
                cmd_vel.angular.z = self.rotation_speed
            else:
                cmd_vel.angular.z = -self.rotation_speed
                
            cmd_vel.linear.x = 0.0
            
            if int(math.degrees(abs(angle_rotated))) % 10 == 0:  # Log cada 10 grados
                self.get_logger().info(f"Rotating: {math.degrees(angle_rotated):.1f}° / {math.degrees(self.target_angle):.1f}°")
        
        self.pub_cmd_vel.publish(cmd_vel)
        
    def get_robot_velocity(self, wl, wr):
        v = self.r * (wl + wr) / 2.0
        w = self.r * (wr - wl) / self.L
        return v, w
        
    def update_robot_pose(self, v, w):
        dt = (self.get_clock().now().nanoseconds - self.prev_time_ns) * 10**-9
        self.x = self.x + v * np.cos(self.theta) * dt
        self.y = self.y + v * np.sin(self.theta) * dt
        self.theta = self.theta + (w * dt)
        self.theta = np.arctan2(np.sin(self.theta), np.cos(self.theta))
        
        self.robot_pose.x = self.x
        self.robot_pose.y = self.y
        self.robot_pose.theta = self.theta

        self.prev_time_ns = self.get_clock().now().nanoseconds

def main(args=None): 
    rclpy.init(args=args) 
    odometry_node = OdometryCross() 
    rclpy.spin(odometry_node) 
    odometry_node.destroy_node() 
    rclpy.shutdown() 

if __name__ == '__main__': 
    main()
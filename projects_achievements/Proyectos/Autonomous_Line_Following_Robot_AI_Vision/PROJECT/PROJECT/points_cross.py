import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Bool, String
import time
import math

class PointsCross(Node):
    def __init__(self):
        super().__init__('points_cross')
        
        # Publishers
        self.move_distance_pub = self.create_publisher(Float32, 'move_distance', 10)
        self.rotate_angle_pub = self.create_publisher(Float32, 'rotate_angle', 10)
        self.crossing_status_pub = self.create_publisher(String, 'crossing_status', 10)
        
        # Subscribers
        self.create_subscription(Bool, 'movement_complete', self.movement_complete_cb, 10)
        self.create_subscription(Bool, 'rotation_complete', self.rotation_complete_cb, 10)
        self.create_subscription(String, "state_crossing", self.state_crossing, 10) 
        self.create_subscription(String, "state_signal", self.state_signal, 10)  # Para recibir direcciones
        

        # Estado del semáforo 
        self.message_light = ''
        self.flag_light = False

        # Estado de la secuencia - AMPLIADO para pausas
        self.sequence_state = 'idle'  # 'idle', 'moving_forward', 'waiting_to_turn', 'turning_left', 'turning_right', 'moving_final', 'moving_through'
        self.sequence_active = False
        self.movement_complete = False
        self.rotation_complete = False
        
        self.message_crossing = ''
        
        # Valor que activará la secuencia
        self.trigger_value = "crossing"
        
        # NUEVO: Control de dirección desde signals
        self.crossing_direction = 'straight'  # 'straight', 'left', 'right'
        self.direction_set = False  # Para saber si ya se estableció la dirección
        
        # Parámetros de movimiento
        self.forward_distance = 0.23  # 27 cm entrada al cruce
        self.through_distance = 0.13  # 13 cm para atravesar derecho
        self.final_distance = 0.15    # 15 cm movimiento final después de girar
        
        # Ángulos de giro
        self.left_turn_angle = (math.pi) * 72 / 180   # +75 grados (izquierda es positivo)
        self.right_turn_angle = (-math.pi) * 65 / 180 # -75 grados (derecha es negativo)
        
        # NUEVO: Timer para pausas controladas
        self.pause_timer = None
        self.pause_duration = 1.0  # 1 segundo de pausa entre movimientos
        self.waiting_for_pause = False
        
        # Timer para controlar la secuencia
        self.timer = self.create_timer(0.1, self.sequence_control)
        
        self.get_logger().info('Points Cross node initialized - PAUSADO MODE')
        self.get_logger().info(f'Waiting for "{self.trigger_value}" message on /state_crossing topic...')
        self.get_logger().info('🎯 Will execute movements step by step with pauses')

    def state_signal(self, data):
        """Callback para recibir señales de dirección desde AI"""
        self.message_signal = data.data
        if self.message_signal == 'Forward':
            self.crossing_direction = 'straight'
            self.direction_set = True
            self.get_logger().info('📍 Direction set to: STRAIGHT')
        elif self.message_signal == 'Left':
            self.crossing_direction = 'left'
            self.direction_set = True
            self.get_logger().info('📍 Direction set to: LEFT')
        elif self.message_signal == 'Right':
            self.crossing_direction = 'right'
            self.direction_set = True
            self.get_logger().info('📍 Direction set to: RIGHT')




    # ==================== FUNCIONES DE MOVIMIENTO ====================
    
    def move_forward(self, distance):
        # Función para mover el robot hacia adelante una distancia específica
        self.get_logger().info(f'Moving forward {distance*100:.1f} cm')
        move_msg = Float32()
        move_msg.data = distance
        self.move_distance_pub.publish(move_msg)
        self.movement_complete = False
    
    def turn_right(self, angle=None):
        # Función para girar el robot a la derecha
        if angle is None:
            angle = self.right_turn_angle
        self.get_logger().info(f'Turning right {abs(math.degrees(angle)):.1f} degrees')
        rotate_msg = Float32()
        rotate_msg.data = angle
        self.rotate_angle_pub.publish(rotate_msg)
        self.rotation_complete = False
    
    def turn_left(self, angle=None):
        # Función para girar el robot a la izquierda
        if angle is None:
            angle = self.left_turn_angle
        self.get_logger().info(f'Turning left {abs(math.degrees(angle)):.1f} degrees')
        rotate_msg = Float32()
        rotate_msg.data = angle
        self.rotate_angle_pub.publish(rotate_msg)
        self.rotation_complete = False

    # ==================== FUNCIONES PARA DIFERENTES DIRECCIONES ====================
    
    def execute_crossing_sequence(self):
        """Inicia la secuencia de cruce (ahora pausada)"""
        direction_name = {'straight': 'STRAIGHT', 'left': 'LEFT', 'right': 'RIGHT'}[self.crossing_direction]
        self.get_logger().info(f'🎯 Starting {direction_name} crossing sequence - PAUSADO MODE!')
        
        # NOTIFICAR QUE INICIA EL CRUCE
        status_msg = String()
        status_msg.data = "crossing_started"
        self.crossing_status_pub.publish(status_msg)
        
        self.sequence_active = True
        self.sequence_state = 'moving_forward'
        self.execute_current_state()

    def state_crossing(self, data): 
        # Callback para recibir mensajes del tópico state_crossing
        self.message_crossing = data.data
        self.get_logger().info(f'Received state_crossing message: "{self.message_crossing}"')
        
        # Activar secuencia si recibe el valor específico y no está ya activa
        if self.message_crossing == self.trigger_value and not self.sequence_active:
            # Ejecutar la secuencia pausada según la dirección
            self.execute_crossing_sequence()

    def movement_complete_cb(self, msg):
        # Callback cuando se completa un movimiento lineal
        if msg.data:
            self.movement_complete = True
            self.get_logger().info('✅ Linear movement completed')

    def rotation_complete_cb(self, msg):
        # Callback cuando se completa una rotación
        if msg.data:
            self.rotation_complete = True
            self.get_logger().info('✅ Rotation completed')

    def start_pause(self, next_state):
        """Inicia una pausa antes del siguiente movimiento"""
        self.waiting_for_pause = True
        self.next_state_after_pause = next_state
        self.pause_start_time = time.time()
        self.get_logger().info(f'⏸️  PAUSING for {self.pause_duration}s before next step...')

    def execute_current_state(self):
        """Ejecuta el comando correspondiente al estado actual"""
        if self.sequence_state == 'moving_forward':
            self.get_logger().info(f'🚶 STEP 1: Moving forward {self.forward_distance*100:.1f} cm (entering crossing)')
            self.move_forward(self.forward_distance)
            
        elif self.sequence_state == 'turning_left':
            self.get_logger().info('🔄 STEP 2: Turning LEFT')
            self.turn_left()
            
        elif self.sequence_state == 'turning_right':
            self.get_logger().info('🔄 STEP 2: Turning RIGHT')
            self.turn_right()
            
        elif self.sequence_state == 'moving_final':
            self.get_logger().info(f'🚶 STEP 3: Moving forward {self.final_distance*100:.1f} cm (final movement)')
            self.move_forward(self.final_distance)
            
        elif self.sequence_state == 'moving_through':
            self.get_logger().info(f'🚶 STEP 2: Moving forward {self.through_distance*100:.1f} cm (going straight through)')
            self.move_forward(self.through_distance)

    def sequence_control(self):
        """Controla la secuencia de movimientos con pausas"""
        if not self.sequence_active:
            return
        
        # Manejar pausas
        if self.waiting_for_pause:
            if time.time() - self.pause_start_time >= self.pause_duration:
                self.waiting_for_pause = False
                self.sequence_state = self.next_state_after_pause
                self.get_logger().info('▶️  PAUSE COMPLETE - Continuing...')
                self.execute_current_state()
            return
            
        # Máquina de estados para la secuencia PAUSADA
        if self.sequence_state == 'moving_forward':
            if self.movement_complete:
                # PAUSA antes de decidir siguiente movimiento
                if self.crossing_direction == 'straight':
                    self.start_pause('moving_through')
                elif self.crossing_direction == 'left':
                    self.start_pause('turning_left')
                elif self.crossing_direction == 'right':
                    self.start_pause('turning_right')
                
        elif self.sequence_state == 'turning_left':
            if self.rotation_complete:
                # PAUSA antes del movimiento final
                self.start_pause('moving_final')
                
        elif self.sequence_state == 'turning_right':
            if self.rotation_complete:
                # PAUSA antes del movimiento final
                self.start_pause('moving_final')
                
        elif self.sequence_state in ['moving_final', 'moving_through']:
            if self.movement_complete:
                # Secuencia completada
                self.sequence_state = 'idle'
                self.sequence_active = False
                
                # 🎉 NOTIFICAR QUE EL CRUCE HA TERMINADO
                status_msg = String()
                status_msg.data = "crossing_complete"
                self.crossing_status_pub.publish(status_msg)
                
                direction_name = {'straight': 'STRAIGHT', 'left': 'LEFT', 'right': 'RIGHT'}[self.crossing_direction]
                self.get_logger().info(f'🎉 {direction_name} crossing sequence completed!')
                self.get_logger().info('📢 Notifying line_follower to resume...')
                self.get_logger().info(f'Waiting for next "{self.trigger_value}" message...')
                
                # Resetear para siguiente cruce
                self.direction_set = False

def main(args=None):
    rclpy.init(args=args)
    points_cross = PointsCross()
    
    try:
        rclpy.spin(points_cross)
    except KeyboardInterrupt:
        pass
    finally:
        points_cross.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    simulation = False
     # NODO 1: Seguimiento de líneas
    line_follower = Node(
        package='PROJECT',
        executable='line_follower_final',
        output='screen',
        emulate_tty=simulation,
        parameters=[
            {'use_sim_time': simulation},
        ]
    )
    # NODO 2: Detección de semáforos
    light = Node(
        package='PROJECT',
        executable='AI',
        output='screen',
        emulate_tty=simulation,
        parameters=[
            {'use_sim_time': simulation},
        ]
    )
    # NODO 3: Detección de señales
    signal = Node(
        package='PROJECT',
        executable='AI2',
        output='screen',
        emulate_tty=simulation,
        parameters=[
            {'use_sim_time': simulation},
        ]
    )
    # NODO 4: Detección de cruces
    crossing = Node(
        package='PROJECT',
        executable='crossing',
        output='screen',
        emulate_tty=simulation,
        parameters=[
            {'use_sim_time': simulation},
        ]
    )
    # NODO 5: Control de movimientos en cruces
    points = Node(
        package='PROJECT',
        executable='points_cross',
        output='screen',
        emulate_tty=simulation,
        parameters=[
            {'use_sim_time': simulation},
        ]
    )
    # NODO 6: Odometría 
    odometry = Node(
        package='PROJECT',
        executable='odometry_cross',
        output='screen',
        emulate_tty=simulation,
        parameters=[
            {'use_sim_time': simulation},
        ]
    )

    return LaunchDescription([
        points,
        odometry,
        line_follower,
        crossing 
    ])
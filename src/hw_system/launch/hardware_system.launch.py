from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='hw_system', executable='emulator_node', name='emulator_node'),
        Node(
            package='hw_system', 
            executable='monitor_node', 
            name='monitor_node',
            parameters=[{'umbral_temperatura': 75}] # Sobrescribir valor por defecto
        ),
        Node(package='hw_system', executable='operator_node', name='operator_node'),
    ])
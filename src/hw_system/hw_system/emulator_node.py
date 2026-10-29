import rclpy
from rclpy.node import Node
import random
from robx7_interfaces.msg import HardwareStatus

class EmulatorNode(Node):
    def __init__(self):
        super().__init__('emulator_node')
        self.publisher = self.create_publisher(HardwareStatus, 'hardware_status', 10)
        self.timer = self.create_timer(1.0, self.publish_status)
        self.temp = 40

    def publish_status(self):
        msg = HardwareStatus()
        self.temp += random.randint(-5, 15)
        if self.temp > 100: self.temp = 40  # Reiniciar ciclo
        
        msg.temperatura = self.temp
        msg.motores_listos = self.temp < 75
        msg.debug_msg = "Operación normal" if msg.motores_listos else "Fallo de sensor / Calentando"
        
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(EmulatorNode())
    rclpy.shutdown()

if __name__ == '__main__':
    main()
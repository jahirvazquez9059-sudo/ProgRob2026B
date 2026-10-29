import rclpy
from rclpy.node import Node
from robx7_interfaces.msg import HardwareStatus
from std_srvs.srv import Trigger

class MonitorNode(Node):
    def __init__(self):
        super().__init__('monitor_node')
        # Parámetro estático (leído solo en inicialización)
        self.declare_parameter('umbral_temperatura', 50)
        self.umbral = self.get_parameter('umbral_temperatura').value
        self.get_logger().info(f"Monitor iniciado. Umbral: {self.umbral}°C")

        self.sub = self.create_subscription(HardwareStatus, 'hardware_status', self.sub_callback, 10)
        self.srv = self.create_service(Trigger, 'check_system', self.check_callback)
        self.last_status = None

    def sub_callback(self, msg):
        self.last_status = msg
        if msg.temperatura > self.umbral:
            self.get_logger().warn(f"ADVERTENCIA: Temperatura ({msg.temperatura}°C) supera el umbral ({self.umbral}°C)")

    def check_callback(self, request, response):
        if not self.last_status:
            response.success = False
            response.message = "Sin datos de hardware"
        elif self.last_status.temperatura > self.umbral or not self.last_status.motores_listos:
            response.success = False
            response.message = "Bloqueo por temperatura alta o motores inactivos"
        else:
            response.success = True
            response.message = "Autorización de movimiento concedida"
        return response

def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(MonitorNode())
    rclpy.shutdown()

if __name__ == '__main__':
    main()
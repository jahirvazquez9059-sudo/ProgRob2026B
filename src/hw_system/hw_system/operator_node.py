import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger

class OperatorNode(Node):
    def __init__(self):
        super().__init__('operator_node')
        self.client = self.create_client(Trigger, 'check_system')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Esperando al nodo monitor...')
        self.timer = self.create_timer(3.0, self.send_request)

    def send_request(self):
        self.client.call_async(Trigger.Request()).add_done_callback(self.response_callback)

    def response_callback(self, future):
        try:
            res = future.result()
            self.get_logger().info(f"Respuesta Monitor: {res.message}")
        except Exception as e:
            self.get_logger().error(f"Error en servicio: {e}")

def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(OperatorNode())
    rclpy.shutdown()

if __name__ == '__main__':
    main()
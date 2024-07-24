# sensors_pkg/motor_encoder_node.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class MotorEncoderNode(Node):
    def __init__(self):
        super().__init__('motor_encoder_node')
        self.publisher_ = self.create_publisher(Int32, 'encoder/data', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Int32()
        # Fill the message with encoder data (this is a placeholder)
        msg.data = 123  # Dummy data for now
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MotorEncoderNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

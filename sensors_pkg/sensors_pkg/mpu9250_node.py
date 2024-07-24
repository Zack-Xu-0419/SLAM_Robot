# sensors_pkg/mpu9250_node.py

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu

class MPU9250Node(Node):
    def __init__(self):
        super().__init__('mpu9250_node')
        self.publisher_ = self.create_publisher(Imu, 'imu/data', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Imu()
        # Fill the message with MPU9250 data (this is a placeholder)
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'imu_link'
        # Add orientation, angular_velocity, linear_acceleration data
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MPU9250Node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

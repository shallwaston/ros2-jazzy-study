import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class FakeOdometryNode(Node):
    def __init__(self):
        super().__init__('fake_odometry_node')

        self.lidar_received_ = False
        self.imu_received_ = False

        self.lidar_subscription_ = self.create_subscription(
            String,
            '/lidar_points',
            self.lidar_callback,
            10,
        )
        self.imu_subscription_ = self.create_subscription(
            String,
            '/imu_data',
            self.imu_callback,
            10,
        )
        self.odom_status_publisher_ = self.create_publisher(String, '/odom_status', 10)

        self.get_logger().info('Subscribing to /lidar_points')
        self.get_logger().info('Subscribing to /imu_data')
        self.get_logger().info('Publishing to /odom_status')

    def lidar_callback(self, msg):
        self.lidar_received_ = True
        self.try_publish_status()

    def imu_callback(self, msg):
        self.imu_received_ = True
        self.try_publish_status()

    def try_publish_status(self):
        if not (self.lidar_received_ and self.imu_received_):
            return

        msg = String()
        msg.data = 'fusion node received lidar and imu'
        self.odom_status_publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = FakeOdometryNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

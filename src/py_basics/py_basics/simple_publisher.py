import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SimplePublisher(Node):
    def __init__(self):
        super().__init__('simple_publisher')

        # 声明 ROS 2 参数，并给出默认值。
        self.declare_parameter('topic_name', 'chatter')
        self.declare_parameter('rate', 1.0)

        self.topic_name_ = self.get_parameter('topic_name').value
        self.rate_ = float(self.get_parameter('rate').value)
        if self.rate_ <= 0.0:
            self.get_logger().warn('Parameter "rate" must be > 0.0, fallback to 1.0 Hz')
            self.rate_ = 1.0

        self.publisher_ = self.create_publisher(String, self.topic_name_, 10)
        self.timer_ = self.create_timer(1.0 / self.rate_, self.publish_message)
        self.count_ = 0

        self.get_logger().info(
            f'Start publishing on /{self.topic_name_} at {self.rate_} Hz'
        )

    def publish_message(self):
        msg = String()
        msg.data = f'Hello ROS 2: {self.count_}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')
        self.count_ += 1


def main(args=None):
    rclpy.init(args=args)
    node = SimplePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

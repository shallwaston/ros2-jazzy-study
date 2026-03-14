import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SimpleSubscriber(Node):
    def __init__(self):
        super().__init__('simple_subscriber')

        # 声明 ROS 2 参数，并给出默认值。
        self.declare_parameter('topic_name', '/chatter')
        self.topic_name_ = self.get_parameter('topic_name').value

        self.subscription = self.create_subscription(
            String,
            self.topic_name_,
            self.listener_callback,
            10,
        )

        self.get_logger().info(f'Start listening on {self.topic_name_}')

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = SimpleSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

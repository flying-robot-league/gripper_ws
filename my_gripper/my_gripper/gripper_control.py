#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from mavros_msgs.msg import CommandLong

class GripperControlNode(Node):
    def __init__(self):
        super().__init__('gripper_control')
        self.publisher = self.create_publisher(CommandLong, '/mavros/cmd/command', 10)

    def set_servo(self, servo_num, pwm):
        msg = CommandLong()
        msg.command = 183  # MAV_CMD_DO_SET_SERVO
        msg.param1 = float(servo_num)  # Servo number, e.g., 9 or 10
        msg.param2 = float(pwm)        # PWM value
        msg.param3 = 0.0
        msg.param4 = 0.0
        msg.param5 = 0.0
        msg.param6 = 0.0
        msg.param7 = 0.0
        msg.confirmation = 0
        msg.broadcast = False
        self.publisher.publish(msg)
        self.get_logger().info(f'Sent command: servo {servo_num} → PWM {pwm}')

def main(args=None):
    rclpy.init(args=args)
    node = GripperControlNode()

    # Example: close gripper on SERVO9 (2000 µs)
    node.set_servo(9, 2000)
    # open gripper on SERVO10 (1000 µs)
    node.set_servo(10, 1000)

    rclpy.spin_once(node, timeout_sec=2.0)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import ParameterDescriptor
from rclpy.time import Time
import tf2_ros
from std_msgs.msg import String, Header
from geometry_msgs.msg import Twist, TwistStamped
from math import sqrt, cos, sin, pi, atan2
from sensor_msgs.msg import LaserScan
import numpy as np
import sys

class PID:
    def __init__(self, Kp, Td, Ti, dt):
        # Note: feel free to rewrite the PID in terms of Kp, Ki, Kd if that is your preferred form
        self.Kp = Kp
        self.Td = Td
        self.Ti = Ti
        self.curr_error = 0
        self.prev_error = 0
        self.sum_error = 0
        self.prev_error_deriv = 0
        self.curr_error_deriv = 0
        self.control = 0
        self.dt = dt
        
    def update_control(self, current_error, reset_prev=False):
        # todo: implement this
        #self.control = ???
        pass
        
    def get_control(self):
        return self.control
        
class WallFollowerHusky(Node):
    def __init__(self):
        # Initialize node and define parameters
        super().__init__('wall_follower_husky')
        self.declare_parameter('forward_speed',0.0)
        self.declare_parameter('desired_distance_from_wall',1.0)

        self.forward_speed = self.get_parameter('forward_speed').value
        self.get_logger().info(f'The value of forward_speed is: {self.forward_speed}')
        self.desired_distance_from_wall = self.get_parameter('desired_distance_from_wall').value
        self.get_logger().info(f'The value of desired_distance_from_wall is: {self.desired_distance_from_wall}')
        
        
        
        # Build a timed operation for PID calculations
        self.timer_hz = 50
        self.pid = PID(1.0, 0.0, 0.0, 1/self.timer_hz)
        
        
        # todo: Build publisher for Husky control commands
        # You'll need to specify the topic you are writing to: /husky_velocity_controller/cmd_vel
        # Kilted requries this to be a "TwistStamped" message type
        
        # self.publisher = 
        
        
        
        
        
        # Set up laser scan subscriber
        # Be sure to use correct function name for the callback that will be run on each laser scan message
        
        # self.laser_sub = 

        
        
              
        
        
        
        
    def laser_scan_callback(self, msg):
        # todo: implement this; ensure you are calling this specific callback for your subscriber node above
        # Populate this command based on the distance to the closest
        # object in laser scan. I.e. compute the cross-track error
        # as mentioned in the PID slides.

        # You can populate the command based on either of the following two methods:
        # (1) using only the distance to the closest wall
        # (2) using the distance to the closest wall and the orientation of the wall
        #
        # If you select option 2, you might want to use cascading PID control. 
  
        
        
        
        # Consider printing a message to show your resulting distance/angle from calculations:
        # self.get_logger().info(f'Received laser scan.  Distance to wall: {min_dist} m, angle: {wall_angle} rad')
        
        
        
        # You need to consruct a stamped Twist message for the robot's velocity controller to use
        outMsg = TwistStamped()
        now = self.get_clock().now()
        outMsg.header.stamp.sec, outMsg.header.stamp.nanosec = now.seconds_nanoseconds()
        outMsg.header.frame_id = 'base_link'
        # outMsg.twist.linear.x = float()  #todo: set forward velocity
        # outMsg.twist.angular.z = float() #todo: from PID
        self.publisher.publish(outMsg)
        pass
   
    
            
            
def main(args=None):
    rclpy.init()
    wfh = WallFollowerHusky()
    rclpy.spin(wfh)
    wfh.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
    



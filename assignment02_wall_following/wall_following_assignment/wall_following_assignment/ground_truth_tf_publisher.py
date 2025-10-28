#!/usr/bin/env python3
import rclpy
import tf2_ros
import sys
import numpy
import tf_transformations
from rclpy.node import Node
from tf2_ros import TransformBroadcaster
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped, Point, Quaternion, PolygonStamped, PointStamped, Point32, TransformStamped


p_map_odom1 = None
q_map_odom1 = None



class GroundTruthTFPublisher(Node):
    def __init__(self):
        super().__init__('ground_truth_tf_publisher')
        self.tf_broadcaster = TransformBroadcaster(self)
        self.declare_parameter('parent_frame_id', 'husky_odom')
        self.declare_parameter('child_frame_id', 'base_link')
        self.odom_sub = self.create_subscription(
            Odometry, #Message type
            'odom',    #Name of topic
            self.odom1_callback,
            10)
        self.get_logger().info(f'Subscribed to /odom topic')



    def odom1_callback(self, msg):
        t = TransformStamped()
        
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'husky_odom'
        t.header.child_frame_id = 'base_link'
        
        
        p = msg.pose.pose.position
        q = msg.pose.pose.orientation
        p_map_baselink = numpy.array([p.x, p.y, p.z])
        q_map_baselink = numpy.array([q.x, q.y, q.z, q.w])

        q_odom1_map = tf_transformations.quaternion_inverse(q_map_odom1)
        R_odom1_map = tf_transformations.quaternion_matrix(q_odom1_map)
        p_odom1_baselink = numpy.dot(R_odom1_map[0:3,0:3], p_map_baselink - p_map_odom1)

        q_odom1_baselink = tf_transformations.quaternion_multiply(q_odom1_map, q_map_baselink)
        
        t.transform.translation = p_odom1_baselink
        t.transform.rotation = q_odom1_baselink

        self.tf_broadcaster.sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    node = GroundTruthTFPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()



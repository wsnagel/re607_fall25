#!/usr/bin/env python3
import rclpy
import tf2_ros
from rclpy.node import Node
import sys
import numpy
from nav_msgs.msg import OccupancyGrid
import pickle



class LoadingOG(Node):
    def __init__(self):
        # Initialize node and define parameters
        super().__init__('occupancy_grid_publisher')
        self.declare_parameter('occupancy_grid_filename','')
        self.occupancy_grid_filename = self.get_parameter('occupancy_grid_filename').value
        self.ogPub = self.create_publisher(OccupancyGrid, 'projected_map', 1)
        
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        
    def timer_callback(self):
        pkl_file = open(self.occupancy_grid_filename, 'rb')
        og = pickle.load(pkl_file)
        #og.header.frame_id = "map"
        
        self.ogPub.publish(og)

 
def main(args=None):
    rclpy.init(args=args)
    node = LoadingOG()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
       


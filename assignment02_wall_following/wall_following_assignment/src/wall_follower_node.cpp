#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/laser_scan.hpp"
#include <geometry_msgs/msg/twist.hpp>
#include <sstream>
#include <cmath>

#include <wall_following_assignment/pid.h>

// Define some values you'll assign in simulation
double desired_distance_from_wall = 0.0; // in meters
double forward_speed = 0.0;              // in meters / sec

using std::placeholders::_1;

class WallFollower : public rclcpp::Node {

public:
  WallFollower() : Node("wall_follower_node") {

    auto default_qos = rclcpp::QoS(rclcpp::SystemDefaultsQoS());

    subscription_ = this->create_subscription<sensor_msgs::msg::LaserScan>(
        "laser_scan", default_qos,
        std::bind(&WallFollower::topic_callback, this, _1));
  }

private:
  void topic_callback(const sensor_msgs::msg::LaserScan::SharedPtr _msg) {
    RCLCPP_INFO(this->get_logger(), "I heard: '%f' '%f'", _msg->ranges[0],
                _msg->ranges[100]);
  }
  rclcpp::Subscription<sensor_msgs::msg::LaserScan>::SharedPtr subscription_;
};




int main(int argc, char **argv) {
  rclcpp::init(argc, argv);
  auto node = rclcpp::Node::make_shared("wall_follower_node");
  

  // Getting params before setting up the topic subscribers
  // otherwise the callback might get executed with default
  // wall following parameters
  
  //forward_speed = this->get_parameter("forward_speed").as_double
  //desired_distance = this->get_parameter("desired_distance_from_wall").as_double

  // todo: set up the command publisher to publish at topic '/husky_1/cmd_vel'
  // using geometry_msgs::Twist messages
  // cmd_pub = ??

  // todo: set up the laser scan subscriber
  // this will set up a callback function that gets executed
  // upon each spinOnce() call, as long as a laser scan
  // message has been published in the meantime by another node
  // ros::Subscriber laser_sub = ??
  
  rclcpp::Rate rate(50);
  
  while (rclcpp::ok()) {
    rclcpp::spin_some(node);
    rate.sleep();
  }
  
  return 0;
}
   

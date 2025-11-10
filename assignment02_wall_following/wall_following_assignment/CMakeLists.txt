cmake_minimum_required(VERSION 3.5)
project(wall_following_assignment)

## Packages from reference
##  cv_bridge
##  geometry_msgs
##  nav_msgs
##  roscpp
##  rospy
##  std_msgs
##  tf

find_package(cv_bridge REQUIRED) 	
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED) 	
find_package(rclcpp REQUIRED)  		
find_package(rclpy REQUIRED)		
find_package(std_msgs REQUIRED)
find_package(tf2 REQUIRED)		
find_package(sensor_msgs REQUIRED)
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(ros_gz_sim REQUIRED)
find_package(ros_gz_bridge REQUIRED)

include_directories(include)

set(
  DEPENDENCIES
  "cv_bridge"
  "geometry_msgs"
  "nav_msgs"
  "rclcpp"
  "rclpy"
  "std_msgs"
  "tf2"
  "sensor_msgs"
  "ros_gz_sim"
  "ros_gz_bridge"
)

## Covered above?  Might have too many dependencies here, keeping this as reference
## ## Generate added messages and services with any dependencies listed here
## generate_messages(
##    DEPENDENCIES
##    geometry_msgs
##    nav_msgs
##    std_msgs
## )



## Declare a C++ executable
add_executable(wall_follower_node
  src/wall_follower_node.cpp)



target_link_libraries(wall_follower_node PUBLIC
	${geometry_msgs_TARGETS}
	${nav_msgs_TARGETS}
	${std_masgs_TARGETS}
	${sensors_msgs_TARGETS}
	cv_bridge::cv_bridge
	rclcpp::rclcpp
	tf2::tf2
	)
	
install(
  TARGETS wall_follower_node
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  wall_following_assignment/ground_truth_tf_publisher.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  wall_following_assignment/wall_follower.py
  DESTINATION lib/${PROJECT_NAME}
)

foreach(dir launch worlds resources urdf models)
  install(DIRECTORY ${dir}/
    DESTINATION share/${PROJECT_NAME}/${dir})
endforeach()




ament_export_include_directories(include)

ament_export_dependencies(${DEPENDENCIES})

ament_python_install_package(${PROJECT_NAME})

ament_package()


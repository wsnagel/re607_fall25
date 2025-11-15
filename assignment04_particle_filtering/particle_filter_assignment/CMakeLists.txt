cmake_minimum_required(VERSION 3.5)
project(particle_filter_assignment)



find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED) 
find_package(rclcpp REQUIRED)  		
find_package(rclpy REQUIRED)	
find_package(tf2 REQUIRED)		
find_package(sensor_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(visualization_msgs REQUIRED)

include_directories(include)

set(
  DEPENDENCIES
  "geometry_msgs"
  "nav_msgs"
  "rclcpp"
  "rclpy"
  "std_msgs"
  "tf2"
  "sensor_msgs"
  "visualization_msgs"
)

install(PROGRAMS
  ${PROJECT_NAME}/monte_carlo_localization.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  ${PROJECT_NAME}/occupancy_grid_publisher.py
  DESTINATION lib/${PROJECT_NAME}
)


foreach(dir launch resources laserControlsOdomData)
  install(DIRECTORY ${dir}/
    DESTINATION share/${PROJECT_NAME}/${dir})
endforeach()


ament_export_include_directories(include)

ament_export_dependencies(${DEPENDENCIES})

ament_python_install_package(${PROJECT_NAME})

ament_package()

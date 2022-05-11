#Description: NOT CURRENTLY USED. Python simulation script that tells Ros2 how to move the robot in a demonstation simulation
#Name: Shea Tanner-Cowie
#Email: st01129@surrey.ac.uk

#! /usr/bin/env python

import rclpy

from rclpy.node import Node
from gazebo_ros_pkgs import gazebo_msg
from gazebo_msgs import srv
from srv import ApplyJointEffort

#name of interface == ApplyJointEffort
 
class effortservice(Node):
 
    def __init__(self):
        # Initialize the node via this constructor
        super().__init__('effort_service')
      
        # Create a service
        self.srv = self.create_service(ApplyJointEffort, 'ApplyJointEffort', self.add_two_ints_callback)
 
    def add_two_ints_callback(self, request, response):
        # Receive the request data and sum it
        response.sum = request.a + request.b
         
        # Return the sum as the reply
        self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))
        return response
 
def main(args=None):
 
    # Start ROS
    rclpy.init(args=args)
 
    # Create the service
    effort_service = effortservice()
 
    # Make the service available to the network
    rclpy.spin(effort_service)
 
    # Shutdown ROS
    rclpy.shutdown()
 
if __name__ == '__main__':
    main()
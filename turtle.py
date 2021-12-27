#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 01:50:49 2021

@author: mustafa
"""

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from math import pow, atan2, sqrt


class TurtleBot:
    
    def __init__(self):
        rospy.init_node('motioncontroller')
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose',Pose,self.update_pose)
        self.goal_pose_subscriber = rospy.Subscriber('/cmd/goal_pose',Pose,self.destination_pose)
        
        self.goal_pose = Pose()
        self.pose = Pose()
        self.rate = rospy.Rate(10)
        
    def destination_pose(self,data):
        self.goal_pose = data
        
    def update_pose(self,data):
        self.pose = data
        
    def mesafe(self,goal_pose):
        return sqrt(pow((goal_pose.x - self.pose.x),2)+pow((goal_pose.y-self.pose.y),2))
    def cizgiselhiz(self,goal_pose,constant=1.5):
        return constant*self.mesafe(self.goal_pose)
    def acisalhiz(self,goal_pose,constant=4):
        return constant * (atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x) - self.pose.theta)
    
    def move_goal(self):
        vel_msg = Twist()
        while not rospy.is_shutdown():
            vel_msg.linear.x = self.cizgiselhiz(self.goal_pose)
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = self.acisalhiz(self.goal_pose)
            
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()
            
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
        rospy.spin()
        
if __name__ == '__main__':
    try:
        x = TurtleBot()
        x.move_goal()
    except rospy.ROSInterruptException:
        pass
    

        

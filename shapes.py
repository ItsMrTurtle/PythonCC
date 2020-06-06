# -*- coding: utf-8 -*-
"""
Created on Thu May 28 15:30:04 2020

@author: Christopher Cheng
"""

class Circle (object):
    def __init__(self):
        self.radius = 0
    def change_radius(self, radius):
        self.radius = radius 
    def get_radius (self):
        return self.radius 

class Rectangle(object):
    # A rectangle object with a width and height
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def set_length(self,length):
        self.length = length
    def set_width(self,width):
        self.width = width

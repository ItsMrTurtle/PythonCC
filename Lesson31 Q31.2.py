# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:43:58 2020

@author: Christopher Cheng
"""
class Rectangle(object):
    # A rectangle object with a width and height
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def set_length(self,length):
        self.length = length
    def set_width(self,width):
        self.width = width
    def get_area(self):
        return self.length * self.width
    def get_perimeter(self):
        return 2*(self.length+self.width)
    
r = Rectangle(1,1)
print("Area:", r.get_area())
print("Perimeter",r.get_perimeter())

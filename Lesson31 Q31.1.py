# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:41:23 2020

@author: Christopher Cheng
"""

class Circle (object):
    # Must initialize parameters of a class afterwards
    # this is aka method 
    # self is used: you'll use this var to refer to any object of type Circle
    def __init__(self):
        # To define an attribute, use self.variable to declare it 
        self.radius = 0
    def change_radius(self, radius): #Using self says we're modifying a data 
        self.radius = radius 
    def get_radius (self): #Use self to access the data, return to public domain 
        return self.radius 
    def get_area (self):
        return 3.14*self.radius**2

test = Circle()
test.change_radius(1)
print(test.get_area())
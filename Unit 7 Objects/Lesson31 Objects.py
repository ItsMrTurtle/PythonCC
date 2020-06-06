# -*- coding: utf-8 -*-
"""
Created on Wed May 20 19:03:34 2020

@author: Christopher Cheng
"""
# Define an object type via class
# parenthesis of object means your class is going to be a python object 
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

class Rectangle(object):
    # A rectangle object with a width and height
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def set_length(self,length):
        self.length = length
    def set_width(self,width):
        self.width = width

a = Rectangle(1,1)
b = Rectangle(1,1)
Rectangle.set_length(a,4)
Rectangle.set_width(b,4)
# one_circle = Circle()
# another_circle = Circle()
# one_circle.change_radius(4)

# print(one_circle.get_radius())
# print(another_circle.get_radius())
       
# # The built in Py method that utilizes self 
# c = Circle()
# c.change_radius(2)
# r = c.get_radius()
# print(r)

# Explict way to refer to a specific object:
c = Circle()
Circle.change_radius(c,2)
r = Circle.get_radius(c)
print(r)
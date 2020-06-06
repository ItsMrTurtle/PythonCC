# -*- coding: utf-8 -*-
"""
Created on Tue May 26 17:50:17 2020

@author: Christopher Cheng
"""
class Stack(object):
    def __init__ (self):
        self.stack = []
    def get_stack_elements(self):
        return self.stack.copy()
    def add_one(self, item):
        self.stack.append(item)
    def add_many(self,item,n): # item is still a single string, n times
        for i in range (n):
            self.stack.append(item)
    def remove_one(self):
        self.stack.pop()
    def remove_many(self,n):
        for i in range(n):
            self.stack.pop()
    def size(self):
        return len(self.stack)
    def prettyprint(self):
        for thing in self.stack[::-1]:
            print("|_", thing,"_|")
    def add_list(self, L):
        for e in L:
            self.stack.append(e)
            
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

# Create 2 stacks of circles and rectangle objects
circles = Stack()
for i in range(3):
    one_circle = Circle()
    one_circle.change_radius(3)
    circles.add_one(one_circle)

rectangles = Stack()
one_rectangle = Rectangle(1,1)
rectangles.add_many(one_rectangle,5)

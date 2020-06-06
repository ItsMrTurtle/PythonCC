# -*- coding: utf-8 -*-
"""
Created on Wed May 27 18:48:24 2020

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
    def __str__ (self):
        ret = ""
        for thing in self.stack[::-1]:
           ret += ("|_" + str(thing) + "_|\n")
        return ret
            
class Circle (object):
    def __init__(self):
        self.radius = 0
    def change_radius(self, radius):
        self.radius = radius 
    def get_radius (self):
        return self.radius 
    def __str__(self):
        return "circle: " + str(self.radius)

circles = Stack()
one_circle = Circle()
one_circle.change_radius(1)
circles.add_one(one_circle)
two_circle = Circle()
two_circle.change_radius(2)
circles.add_one(two_circle)
print(circles)
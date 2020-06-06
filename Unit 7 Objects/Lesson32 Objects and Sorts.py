# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:47:05 2020

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

# Using an object for objects 
circles = Stack()
one_circle = Circle()
one_circle.change_radius(2)
circles.add_one(one_circle)

# For loop method, has all differment memory locations 
# for i in range(5):
#     one_circle = Circle()
#     one_circle.change_radius(1)
#     circles.add_one(one_circle)
    
# Instead of a for loop, can use the add_many method:
# Has the same memory location since its adding the same object 
one_circle = Circle()
one_circle.change_radius(1)
circles.add_many(one_circle,5)

print(circles.size())
circles.prettyprint()

# Adding to a list via string objects 
# pancakes = Stack()
# pancakes.add_one("blueberry")
# pancakes.add_many("chocolate", 4)
# print(pancakes.size())
# pancakes.remove_one()
# print(pancakes.size())
# pancakes.prettyprint()
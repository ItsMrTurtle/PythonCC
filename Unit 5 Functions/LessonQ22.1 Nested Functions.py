# -*- coding: utf-8 -*-
"""
Created on Thu May  7 18:14:22 2020

@author: Christopher Cheng
"""
# No need for an if statement, the shape variable takes the name of the function

def area(shape,n):
    return shape(n)

def circle(radius):
    return 3.14*radius**2
def square(length):
    return length**2

print(area(circle,5))
print(area(circle,10))
print(area(square,5))
print(area(circle,4/2))
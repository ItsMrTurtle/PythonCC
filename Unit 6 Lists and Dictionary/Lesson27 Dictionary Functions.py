# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:59:10 2020

@author: Christopher Cheng
"""

def square(x):
    return x*x

def circle(r):
    return 3.14*r*r

def equal_tri (s):
    return (s*s)*(3**0.5)/4

# The value is the function mapped 
areas = {"sq": square, "ci": circle, "eqtri": equal_tri}

# When accessing the dictionary keys, you can pass a parameter if it's a function 
n = 2
print(areas["sq"](n))
print(areas["ci"](n))
print(areas["eqtri"](n))
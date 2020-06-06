# -*- coding: utf-8 -*-
"""
Created on Sun May 10 01:15:55 2020

@author: Christopher Cheng
"""

# Modifying List Items 

colors = ["red","blue","yellow"]
colors[0] = "orange" # Changes red to orange 
print(colors)

colors[1] = "green"
print(colors)

colors[2] = "purple"
print(colors)

colors[-1] = colors[0]
print(colors)
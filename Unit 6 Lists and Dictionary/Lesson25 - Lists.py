# -*- coding: utf-8 -*-
"""
Created on Fri May  8 22:30:39 2020

@author: Christopher Cheng
"""

# Immutable: Value can't change 
# Use the function: append to add to a tuple 
# THis keeps the memory intact 

a = ["milk","eggs"]
print(id(a))

a.append("bread")
print(id(a))

grocery = ["turts", "clem", "alex"]
# can do length of a lsit for number of objects in a list
print(len(grocery))
print(grocery[0])
print(grocery[1])
print(grocery[2])
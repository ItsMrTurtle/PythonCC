# -*- coding: utf-8 -*-
"""
Created on Sun May 10 00:50:49 2020

@author: Christopher Cheng
"""
# Adding stuff to lists 

# Append to list
# Can only append one item at a time 
# Appends to the end of a list 
grocery = []
grocery.append("eggs")
print(grocery)

# Insert to list
# L.insert(i,e) insert element e at index i 
# One item at a time 
# Shifts all elements over 
grocery.insert(0,"turts")
print(grocery)

# Extend to list 
# L.extend(M) appends all items from list M to the end of L 
# M remains unchanged 
burger = ["lettuce", "tomato","mayo"]
grocery.extend(burger)
print(grocery)

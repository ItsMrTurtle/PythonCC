# -*- coding: utf-8 -*-
"""
Created on Sun May 10 01:54:54 2020

@author: Christopher Cheng
"""
# Sorting Lists

L = []

# To sort: L.sort()
# Sorts numbers in ascending order 
# Sorts lexicographically for letters 

# To reverse a list: L.reverse()

heights = [1.4,1.3,1.5,2,1.4,1.5,1]
heights.reverse() #Reverse the original 
print(heights)

# Sort is ascending order
heights.sort()
print(heights)

# Reversing this sorts in descending order cause it was once sorted 
heights.reverse()
print(heights)

L = ["p","r","o","g","r","a","m","m","i","n","g"]
print(L)
L.reverse()
print(L)
L.sort()
print(L)
L.reverse()
print(L)
L.reverse()
print(L)
L.sort()
print(L)
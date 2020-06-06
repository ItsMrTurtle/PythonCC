# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:53:01 2020

@author: abcdk
"""

a = float(input("Enter your first number: "))
b = float(input("Enter your second number: "))

if a == b:
    print(a,"is equal to",b)
elif a > b:
    print("First num is greater than the second")
else:
    print("First num is LESS than the second")
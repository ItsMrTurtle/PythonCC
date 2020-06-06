# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 22:57:02 2020

@author: Christopher Cheng
"""

num = int(input("Enter a number between 1 and 14: "))
trial = 1
code = 7

while num != code:
    print("Wrong, try again. This is trial number:", trial)
    num = int(input("Enter a number between 1 and 14: "))
    trial += 1
    
print("You guessed right, my number was", code)
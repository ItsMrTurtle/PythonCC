# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 23:20:43 2020

@author: Christopher Cheng
"""

guess = input("Enter the password: ")
code = "turtle"

trial = 1
maxTries = 3

while guess != code:
    if trial >= maxTries:
        break
    trial +=1
    guess = input("Enter again: ")

if (trial >= maxTries):
    print("Took too long...")
    
else:
    print("Nice, you got it")
        
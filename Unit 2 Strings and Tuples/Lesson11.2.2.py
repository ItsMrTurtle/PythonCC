# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:41:50 2020

@author: abcdk
"""

# Input Commands

name = input("What is your name? ")
age = int(input("How old are you? "))

fName = name.capitalize() + "!"
fAge = str(age+25) + "!"


print("Hi",fName,"In 25 years you will be",fAge)

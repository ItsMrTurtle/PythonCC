# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 23:26:25 2020

@author: abcdk
"""

countEven = 0
countDiv = 0

for i in range(2,100,2):
    countEven += 1
    if i%6 == 0:
        countDiv += 1

print("Number of Even numbers:", countEven)
print("Number of Divisions by 6:", countDiv)

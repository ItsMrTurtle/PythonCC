# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 23:05:18 2020

@author: Christopher Cheng
"""
# Rewrite a while loop into a for loop

password = "robot fort flower graph"
characters = len(password)
gap = 0

for i in range (characters):
    if password[i] == " ":
        gap += 1

print("Num spaces:",gap)

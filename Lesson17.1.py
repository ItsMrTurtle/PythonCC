# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 22:54:03 2020

@author: abcdk
"""
# range(start,end,step)
# End is NOT INCLUSIVE
# Can do negative steps

# Just 1: End num. Start = 0, step = 1.
# Just 2: Start, End. step = 1

word = input("Enter a word! ")

for i in word:
    if i == "a" or i == "e" or i =="i" or i == "o" or i =="u":
        print(i, "is a vowel")
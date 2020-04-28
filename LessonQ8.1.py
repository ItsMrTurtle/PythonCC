# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 23:45:01 2020

@author: abcdk
"""

# Compelx Strings and Substrings 
# "var".find() and "var".rfind()
# "test" in "var" gives a boolean if the word is a subset or not

word = "Eat Work Play Sleep repeat"

word = word.replace(" ", "ing ")
word = word[7:22]
word = word.lower()
print(word)

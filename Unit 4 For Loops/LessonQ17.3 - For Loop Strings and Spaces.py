# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 00:46:10 2020

@author: Christopher Cheng
"""

names = input("Enter names seperated by a single space: ")
# Initialize the variable
word = ""

# Iterate through the bunch of names
for i in names:
    # If not a space, combine to collect the letters of the name
    if i != " ":
        word = word + i
    #If space, print the word to cash out, then reset the variable
    elif i == " ":
        print("Hi", word)
        word = ""

print ("Hi", word) #Print the final name
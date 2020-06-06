# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 23:29:35 2020

@author: Christopher Cheng
"""

# Continues are used in place of nested if statements to make the code look cleaner
# if-if-if can be replaced by continue
# If the if statement is true, continue towards the next statements 

code = 7
go = input("Do you want to play a game? (yes or y): ")
play = True

while play:
    if go =="yes" or go == "y":
        num = int(input("Enter a number between 1 and 10: "))
        while code != num:
            num = int(input("Keep guessing! "))
        print("Nice, you got it!")
        go = input("Do you want to play again? (yes or y): ")
    else:
        play = False

print("No play :(")
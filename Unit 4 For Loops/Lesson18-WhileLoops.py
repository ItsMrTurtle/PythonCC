# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:15:54 2020

@author: Christopher Cheng
"""

secret = "code"
guess = input("Guess a word: ")
tries = 1

while guess != secret:
    print("You tried to guess", tries, "times")
    guess = input("Guess again: ")
    tries += 1

print ("Niceee, you got it")
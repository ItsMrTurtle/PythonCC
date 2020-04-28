# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:57:16 2020

@author: abcdk
"""
word = input("Enter a word: ")

if "a" in word and "e" in word and "i" in word and "o" in word and "u" in word:
    print("you have all the vowels!")
    if word[0] == "a" and word[len(word)-1] =="z":
        print("And it's sort of alphabetical!")
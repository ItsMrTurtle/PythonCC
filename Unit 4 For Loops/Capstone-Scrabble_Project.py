# -*- coding: utf-8 -*-
"""
Created on Fri May  1 00:11:16 2020

@author: Christopher Cheng
"""
##### Get back to this
# Capstone Project -Simple Scrabble Version

# Set a word bank of legal words. These are seperated by lines under one string
# We can use a triple quote to capture line breaks in a string

bank = """art
hue
ink
oil
pen
wax
clay
draw
film
crosshatching
"""
# Initialize this tuple of seperated words from the word bank
valid_Words = ()
temp = ""
for char in bank:
    if char != "\n":
        temp += char
    else:
        valid_Words += (temp,)
        temp = ""
 
# Textbook version to parse words from the word bank 
# start = 0
# end = 0       
# for char in bank:
#     if char == "\n":
#         valid_Words += (bank[start:end],)
#         start = end + 1
#         end = end + 1
#     else:
#         end = end + 1
        

# Given tiles, a user inputted scrabble of letters
tiles = input("Enter your tiles: ")

# Initialize the tuple of matched words with the tiles and work bank
match = ()

# Determine if your tiles match the words in the word bank 
# Remove them from play. Make sure it's a 1 to 1 use.

for word in valid_Words:
    tiles_left = tiles
    for letter in word:
        if letter not in tiles_left:
            break
        else:
            index = tiles_left.find(letter)
            tiles_left = tiles_left[:index]+tiles_left[index+1:]
    if len(word) == len(tiles) - len(tiles_left):
        match = match + (word,)
print(match)
    

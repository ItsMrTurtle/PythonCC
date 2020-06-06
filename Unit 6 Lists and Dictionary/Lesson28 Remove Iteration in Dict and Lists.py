# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:05:34 2020

@author: Christopher Cheng
"""

# Can't change the dictionary size when you're itterating through it 
# Will get an error when running this 

# songs = {"Wannabe": 1, "Roar": 1, "Let it be":5, "Red Corvette": 4}

# for s in songs:
#     if songs[s] == 1:
#         songs.pop(s)


# Buggy if removing things from a LIST when itterating through it 
# When itterating through it, it's index count doesn't adjust 
fsongs = [1,1,5,4]

for s in fsongs :
    if s ==1:
        fsongs.pop(s)
print (fsongs) # Still prints [1,5,4] FOR SOME REASON?????????

# To remove items from a list or a dict, must make a copy of it 

songs = [1,1,5,4]
songs_copy = songs.copy()
songs = []

# Have to play around with 2 objects. 
for s in songs_copy:
    if s!= 1:
        songs.append(s)
print(songs)
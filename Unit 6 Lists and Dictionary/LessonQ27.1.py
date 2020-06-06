# -*- coding: utf-8 -*-
"""
Created on Sun May 10 23:25:48 2020

@author: Christopher Cheng
"""

songs = {"turts":5, "neyo":3,"drake":4, "chrisJam":5}
good_songs = {}

print("The following songs are 5 star ratings: ")

for i in songs.keys():
    if songs[i] == 5:
        print(i)
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:49:04 2020

@author: Christopher Cheng
"""

# Dictionaries are good because they can map and trace
# They can keep count and map to functions

lyrics = "Happy birthday to you Happy birthday to you Happy birthday dear Happy birthday to you"
counts = {}

words = lyrics.split(" ")
for w in words:
    w = w.lower()
    if w not in counts:
        counts[w] = 1
    else:
        counts[w] += 1

print(counts)
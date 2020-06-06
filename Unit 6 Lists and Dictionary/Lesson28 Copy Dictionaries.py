# -*- coding: utf-8 -*-
"""
Created on Tue May 12 18:48:10 2020

@author: Christopher Cheng
"""

# By setting a new variable and casting the dictionary into a list form,
# Can make a new copy of it 

artists = ["monet", "picasso"]
painters = list(artists)
painters.append("van gogh")

# If list, can also use .copy() function 
# This is another way that acheives the same thing 
lala = ["turt","clemm"]
bobo = lala.copy()
bobo.append("plush")

# Can sort and copy at the same time via sorted(L)
# Rather than using .sort(), which changes the pointer and sorts the original 
kids_age = [2,1,4]
sorted_age = sorted(kids_age)

# QC 28.4 
chaos = []
order = sorted(chaos)

colors = []
colors.sort()

cards = []
deck = cards
cards = cards.sort()
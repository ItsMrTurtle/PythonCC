# -*- coding: utf-8 -*-
"""
Created on Sun May 10 01:20:27 2020

@author: Christopher Cheng
"""

##* IF YOU APPEND A LIST, THE LIST IS JUST ONE OBJECT

menu = []

# Part 1
menu.append("pizza")
menu.append("beer")
menu.append("fries")
menu.append("wings")
menu.append("salad")
print(menu)

# Part 2
menu[0] = menu[-1]
menu.pop(1)
menu[-1] = "pizza"
print(menu)

# Part 3
menu[1] = "quinoa"
menu[2] = "steak"
menu.pop()
print(menu)
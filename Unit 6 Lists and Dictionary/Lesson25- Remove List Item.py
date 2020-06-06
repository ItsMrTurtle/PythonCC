# -*- coding: utf-8 -*-
"""
Created on Sun May 10 00:59:19 2020

@author: Christopher Cheng
"""

# Can remove items from a list with function L.pop()
# Blank () removes the last item in the list 
# O/w can specify index to remove L.remove(i)
# Returns the item that you deleted

polite = ["please", "thank you", "and", "pls"]
print(polite.pop())
print(polite)
print(polite.pop(1))
print(polite)
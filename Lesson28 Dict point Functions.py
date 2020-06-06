# -*- coding: utf-8 -*-
"""
Created on Mon May 11 01:46:35 2020

@author: Christopher Cheng
"""

# If 2 you make a var point at a dict
# Say L and M

L = {}
M = L

# Changing M will also change L since they point at the same thing 
# Does NOT apply to lists though 

# Passing a dict in a function is like passing it globally 


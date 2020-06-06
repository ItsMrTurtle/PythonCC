# -*- coding: utf-8 -*-
"""
Created on Sun May 10 23:31:38 2020

@author: Christopher Cheng
"""

def replace (d, v, e):
    """
    d is a dictionary
    v,e are 2 values
    Goal: Replace all values v with the string e in dictionary d
    Returns nothing
    """
    # Altering a dictionary in a function will change it globally 
    for num in d.keys():
        if d[num] == v:
            d[num] = e

di = ({1:2, 3:1, 4:2})
print(di)
replace(di,1,2)
print(di)

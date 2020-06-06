# -*- coding: utf-8 -*-
"""
Created on Sun May 10 23:48:53 2020

@author: Christopher Cheng
"""

def invert(d):
    """
    Take in dictionary d
    Returns a new dictionary: d_inv 
    Values in it are a list 
    Flips value and keys 
    """
    d_Inv = {}
    for i in d.keys():
        temp = d[i]
        
        # Need the if statement to assign, or add to a list! 
        if temp not in d_Inv:
           d_Inv[temp] = [i]
        else:
            d_Inv[temp].append(i)
    return d_Inv

L = ({1:1,3:1,5:1})
print(L)
print(invert(L))
    

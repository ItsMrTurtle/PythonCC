# -*- coding: utf-8 -*-
"""
Created on Sun May 10 01:34:51 2020

@author: Christopher Cheng
"""

def unique(L):
    """
    L is a list
    Return unique elements in L
    """
    unique = []
    for i in L:
        if i not in unique:
            unique.append(i)
    return unique
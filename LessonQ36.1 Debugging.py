# -*- coding: utf-8 -*-
"""
Created on Sat May 30 14:20:41 2020

@author: Christopher Cheng
"""

def remove_buggy(L, e):
    """
    L, list
    e, any object
    Removes all e from L.
    """
    # Making changes to items removed from a lsit messes it up
    for i in L.copy():
        if e == i:
            L.remove(i)

L = [1,1,1,2,2,3,2,2,1,1,1]
remove_buggy(L,1)

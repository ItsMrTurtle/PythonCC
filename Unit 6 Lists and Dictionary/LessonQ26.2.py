# -*- coding: utf-8 -*-
"""
Created on Sun May 10 18:37:59 2020

@author: Christopher Cheng
"""

def is_permutation (L1,L2):
    L1.sort()
    L2.sort()
    return L1 == L2

print(is_permutation([1,2,3,1],[1,2,3]))


# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:45:18 2020

@author: Christopher Cheng
"""

def invert_dict_inplace (L):
    """

    Parameters
    ----------
    L : TYPE Dictionary
       Swaps values and keys without a copy 

    Returns
    -------
    None.

    """
    new_L = L.copy()
    L = {}
    for k in new_L.keys():
        L[new_L[k]] = k
    print(L)

d = {1:100,2:200,3:300}
invert_dict_inplace(d)
print(d)
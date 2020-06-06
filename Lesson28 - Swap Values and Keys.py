# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:20:02 2020

@author: Christopher Cheng
"""


def invert_dict (d):
    """

    Parameters
    ----------
    L : TYPE Dictionary 
        Swaps keys and values 

    Returns
    -------
    New dictionary with swapped values and keys 

    """
    new_d = {}
    for k in d.keys():
        new_d[d[k]] = k
    return new_d

d = {1:100,2:200,3:300}
print(invert_dict(d))
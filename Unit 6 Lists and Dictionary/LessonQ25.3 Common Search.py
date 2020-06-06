# -*- coding: utf-8 -*-
"""
Created on Sun May 10 01:38:13 2020

@author: Christopher Cheng
"""

def common (L1,L2):
    isTrue = True
    for i in L1:
        if i not in L2:
            return False
    for j in L2:
        if j not in L1:
            return False
    return isTrue

list1 = [1,2,3]
list2 = [1,3,2]
print(common(list1,list2))

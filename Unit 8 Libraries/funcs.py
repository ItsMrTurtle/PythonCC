# -*- coding: utf-8 -*-
"""
Created on Thu May 28 18:02:27 2020

@author: Christopher Cheng
"""

def is_prime(n):
    prime = True
    for i in range(2,n):
        if n%i == 0:
            prime = False
        return prime

def abs_val (n):
    if n< 0:
        return -n
    else:
        return n

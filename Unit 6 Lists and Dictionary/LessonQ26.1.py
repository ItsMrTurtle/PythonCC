# -*- coding: utf-8 -*-
"""
Created on Sun May 10 18:33:52 2020

@author: Christopher Cheng
"""


def sort_Lists (cities): 
    """
    cities is a string of cities under 1 string, spearated by commas
    """
    L = cities.split(",")
    L.sort()
    print(L)

cities = "san francisco,boston,chicago,indianapolis"
sort_Lists(cities)
    
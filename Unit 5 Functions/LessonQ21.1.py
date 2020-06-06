# -*- coding: utf-8 -*-
"""
Created on Thu May  7 18:04:54 2020

@author: Christopher Cheng
"""

def calculate_total (price, percent):
    """
    
    Parameters
    ----------
    price : TYPE float
    percent : TYPE integer

    Returns
    -------
    New number showing the price + the tip
    Should return number as a FLOAT

    """
    total = price + price*percent/100
    return total

my_price = 78.55
my_percent = 20
print("Total is: $", calculate_total(my_price,my_percent))
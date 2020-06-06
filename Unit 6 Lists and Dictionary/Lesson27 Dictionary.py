# -*- coding: utf-8 -*-
"""
Created on Sun May 10 18:56:53 2020

@author: Christopher Cheng
"""

# Dictionary type dict
# 2 inputs: key and value, {}

grocery = {}
grocery = {"milk":1,"eggs":12,"bread":2}

# To add to the end of the dictionary
grocery["k"] = "lala"

# To edit: 
# Keys must be unique 
grocery["k"] = "turts"
print(grocery)

# To remove from dictionary
# Use .pop("key") same like lists but use the key instead of index
grocery.pop("eggs")
print(grocery)

# To get all dictionary keys:
# Returns a list of all keys as a Python object 
# Can iterate through them like: for i in dict.keys()
print(grocery.keys())

# Can cast the results into a list 
all_keys = list(grocery.keys())

# Can also do grocery.values() to get a Python object of the values 
# *** But no traceability back to the dictionary! 
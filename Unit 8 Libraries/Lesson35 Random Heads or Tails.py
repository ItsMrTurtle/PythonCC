# -*- coding: utf-8 -*-
"""
Created on Thu May 28 16:50:09 2020

@author: Christopher Cheng
"""

import random

heads = 0
tails = 0

for i in range(100):
    r = random.random()
    if r < 1/2:
        heads += 1
    else:
        tails += 1

print("Heads in 100 trials:",heads)
print("Tails in 100 trials:",tails)

print(random.randint(2,17))
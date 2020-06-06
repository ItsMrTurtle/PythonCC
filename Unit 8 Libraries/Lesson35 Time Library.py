# -*- coding: utf-8 -*-
"""
Created on Thu May 28 16:55:36 2020

@author: Christopher Cheng
"""

import time
import random

# starts the current time in ms
start = time.process_time()

count = 0
for i in range(1000000):
    count += 1

# Gets the current time in ms
end = time.process_time()
print(end-start) # Get the difference in times 

t1 = time.process_time()
turts = []
for i in range (1000000):
    r = random.random()

t2 = time.process_time()
print("Time is:", t2-t1)
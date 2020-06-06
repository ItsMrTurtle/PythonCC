# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:08:30 2020

@author: Christopher Cheng
"""

import time 

print("Loading...")
for i in range(10):
    print("[",i*"*",(10-i)*" ","]",i*10,"% Complete")
    time.sleep(0.5)
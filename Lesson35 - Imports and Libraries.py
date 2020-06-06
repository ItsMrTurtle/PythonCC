# -*- coding: utf-8 -*-
"""
Created on Thu May 28 15:30:56 2020

@author: Christopher Cheng
"""

import math

distance = float(input("How far away is your friend? (in metres): "))
speed = float(input("How fast can you throw? (m/s): "))
tolerance = 2

for deg in range(91):
    # Convert from deg to rad
    angle_rad = math.radians(deg)
    
    # Use the math library to calculate the reach 
    reach = 2*speed**2*math.sin(angle_rad)*math.cos(angle_rad)/9.8
    
    if reach > distance - tolerance and reach < distance + tolerance:
        print(deg, "Good throw")
    
    elif reach < distance - tolerance:
        print(deg, "Not far enough")
        
    else:
        print(deg, "You threw too far")
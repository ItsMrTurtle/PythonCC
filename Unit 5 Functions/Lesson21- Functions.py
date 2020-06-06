# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:06:28 2020

@author: Christopher Cheng
"""

def take_attendance(classroom,"who_is_here"):
    """
    classroom, tuple
    who_is_here, tuple
    Checks if every item in classroom is in who_is_here
    Prints their name if so
    Returns "finished taking attendance"
    """
    for kid in classroom:
        if kid in who_is_here:
            print(kid)
    return "finished taking attendance"

# def set_color(name, color)
    #name, string
    #color, string

# def get_inverse (num)
    # num, float

# def print_my_name()

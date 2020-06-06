# -*- coding: utf-8 -*-
"""
Created on Thu May  7 19:07:17 2020

@author: Christopher Cheng
"""
# To use nested functions, must return the nested function in order to call and use it

def person(age):
    print("I am a person")
    def student(major):
        print("I like learning")
        def vacation(place):
            print("But I need to take breaks")
            print(age,"|",major,"|",place)
        return vacation
    return student
            
person(12)("Math")("Beach")
person(29)("CS")("Japan")
person(23)("Law")("Florida")

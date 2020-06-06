# -*- coding: utf-8 -*-
"""
Created on Tue May 26 18:15:08 2020

@author: Christopher Cheng
"""

class Fraction (object):
    def __init__ (self, top, bottom):
        self.top = top
        self.bottom = bottom 
        
    def __add__ (self, other_fraction):
        new_top = self.top*other_fraction.bottom + \
            self.bottom*other_fraction.top
        new_bottom = self.bottom * other_fraction.bottom
        return Fraction(new_top, new_bottom)
    
    def __mul__(self, other_fraction):
        new_top = self.top * other_fraction.top 
        new_bottom = self.bottom * other_fraction.bottom
        return Fraction(new_top, new_bottom)
    
    def __sub__(self, other_fraction):
        new_top = self.top*other_fraction.bottom - \
            self.bottom*other_fraction.top
        new_bottom = self.bottom * other_fraction.bottom
        return Fraction(new_top, new_bottom)
    
    # Altering __str__ allows it to print the values we want 
    def __str__ (self):
        return str(self.top) + "/" + str(self.bottom)
        
half = Fraction(1,2)
quarter = Fraction(1,4)
# print(half + quarter)

#1 quarter * half:
print(Fraction.__mul__(half,quarter))
print(half.__mul__(quarter))

#2 print(quarter)
print(Fraction.__str__(quarter))
print(quarter.__str__())

#3 print(half*half)
print(Fraction.__mul__(half,half))
print(half.__mul__(half))
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 23:10:39 2020

@author: abcdk
"""

hungry = input("Are you hungry? (yes or no): ")
price = float(input("Price of cholcolate bar: "))
bars = 0

if hungry.lower() == "yes":
    if price < 1:
        print("100 it is")
        bars = 100
    if 1 < price < 5:
        print("We saving,; 10 it is")
        bars = 10
    if price > 5:
        print("wtf too expensive")
        bars = 1

if hungry.lower() == "no":
    bars = 0

if bars > 11:
    print("Fatty")

print("You checked out", bars)
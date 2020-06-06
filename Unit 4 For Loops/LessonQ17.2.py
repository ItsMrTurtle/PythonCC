# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 00:10:52 2020

@author: Christopher Cheng
"""

num = int(input("Enter the number of books on the shelf: "))
i = num

for i in range (num,0,-1):
   
    if i == 1:
        print(i,"book on Python on the shelf", i, "book on Python")
        print("Take one down, pass it around, no more books!")
        
    else:
        print(i,"books on Python on the shelf", i, "books on Python")
        print("Take one down, pass it around,",i-1,"books left")

# -*- coding: utf-8 -*-
"""
Created on Sun May 10 17:58:00 2020

@author: Christopher Cheng
"""

# Empty set of lists
L = [[],[],[]]
L[0] = [1,2,3]
L[1].append("T")
L[1].append("o")
L[1][0] = "d"

print(L)

game = [[],[],[]]
x = "x"
o = "o"
empty = "_"

game = [[empty,empty,empty],[x,x,x],[o,o,o]]
print(game[0])
print(game[1])
print(game[2])

game = [[x,o,x,o],[o,o,x,x],[o,empty,x,x]]
print(game[0])
print(game[1])
print(game[2])
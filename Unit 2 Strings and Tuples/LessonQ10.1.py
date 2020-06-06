# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 01:19:48 2020

@author: abcdk
"""

word = "echo"
t = ()
count = 3

# t0 = (word[0:4] *count)
# t1 = (word[1:4] *count)
# t2 = (word[2:4] *count)
# t3 = (word[3:4] *count)

# t = (t0, t1, t2, t3)

# print(t)

t0 = (word,) * count
t1 = (word[1:],) * count
t2 = (word[2:],) * count
t3 = (word[3:],) * count

t = (t0,t1,t2,t3)

print (t)
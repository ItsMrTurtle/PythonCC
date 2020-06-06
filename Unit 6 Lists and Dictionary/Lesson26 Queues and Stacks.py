# -*- coding: utf-8 -*-
"""
Created on Sun May 10 18:18:28 2020

@author: Christopher Cheng
"""

# Stacks 
# Last in, First out / First in Last Out
# Utilizes L.append() and L.pop()

stack = []
cook = ["blueberry","blueberry","blueberry"]
stack.extend(cook)
stack.pop()
stack.pop()
cook = ["chocoloate","chocolate"]
stack.extend(cook)
stack.pop()
cook = ["blueberry","blueberry"]
stack.extend(cook)
stack.pop()
stack.pop()
stack.pop()

# Queues are the opposite
# First in is the First Out 
# Utilizes L.append() and more important L.pop(0)

line = []
line.append("Ana")
line.append("Bob")
line.pop(0)
line.append("chris")
line.append("turts")
line.pop(0)
line.pop(0)
line.pop(0)

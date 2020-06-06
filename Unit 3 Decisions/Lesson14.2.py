# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:15:57 2020

@author: abcdk
"""
# Conditional if statements with 2 conditions 
# and + or

greeting = input("Say hi in English or Spanish: ")
greet_en = ("Hi", "Hello", "hi", "hello")
greet_sp = ("hola", "Hola")

if greeting not in greet_en and greeting not in greet_sp:
    print("Speak the langugage bruh")
    
elif greeting in greet_en:
    print("Ayyy English")
    num = int(input("Enter 1 or 2: "))
    if num == 1:
        print("One")
    elif num ==2:
        print("Two")
    else:
        print("??? u drunk")

elif greeting in greet_sp:
    print("Mi Spanish nana")
    num = int(input("Enter 1 or 2: "))
    if num == 1:
        print("Uno")
    elif num ==2:
        print("Dos")
    else:
        print("???? nani")
        
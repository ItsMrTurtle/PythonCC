# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 18:10:51 2020

@author: abcdk
"""
#Input First Last
#Input First Last

#Output First Last
## Mixture of first names, and mixtures of last name 

# Goal: Receive inputs and mix them up 

#---------------------------------------------------------------------------

#Input First Name and Last name for 2 names 
print("Welcome to my Mashup Capstone Project!")
name1 = input("Enter the name of guy #1 (First Last): ")
name2 = input("Enter the name of guy #2 (First Last): ")

#First Name 1
fName1_index = name1.find(" ")
fName1 = name1[0:fName1_index]

#Last Name 1
lName1 = name1[fName1_index+1:len(name1)]

#First Name 
fName2_index = name2.find(" ")
fName2 = name2[0:fName2_index]

#Last Name 2
lName2 = name2[fName2_index+1:len(name2)]

#Mixed First Name
# number of letters (1/2) for midPt -- Do first name first rn
mid_f1 = int(len(fName1)/2)
mid_f2 = int(len(fName2)/2)
mash_first = fName1[0:mid_f1] + fName2[mid_f2:len(fName2)]

# Mixed Last Name -- 1st Name first 
mid_l1 = int(len(lName1)/2)
mid_l2 = int(len(lName2)/2)
mash_last = lName1[0:mid_l1] + lName2[mid_l2: len(lName2)]

# Mashed Name Message
print("Your mashed name is!: ")
print(mash_first.capitalize(), mash_last.lower())

#Alt Name 
aFirst = fName2[0:mid_f2] + fName1[mid_f1:len(fName1)]
aLast = lName2[0:mid_l2] + lName1[mid_l1:len(lName1)]

print("Your alt name is: ")
print(aFirst.capitalize(), aLast.lower())
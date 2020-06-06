# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:32:15 2020

@author: Christopher Cheng
"""
grades = {}
grades["Chris"] = [100,100]
grades["Angela"] = [90,100]
grades["Bruce"] = [80,40]
grades["Stacey"] = [70,70]

for student in grades:
    print(student)

for quizzes in grades.values():
    print(sum(quizzes)/2)

for student in grades.keys():
    scores = grades[student]
    grades[student].append(sum(scores)/2) #Interesting useage... 

print(grades)
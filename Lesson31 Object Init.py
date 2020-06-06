# -*- coding: utf-8 -*-
"""
Created on Wed May 20 19:22:00 2020

@author: Christopher Cheng
"""

class Person (object):
    def __init__ (self):
        self.age = 0
        self.height = 0
        self.weight = 0

class car (object):
    def __init__ (self):
        self.hp = 0
        self.doors = 0
        self.color = "blue"

class computer (object):
    def __init__ (self):
        self.cpu = "AMD"
        self.screen = 0
        self.power = "On"

class Door(object):
    def __init__(self):
        self.width = 1
        self.height = 1
        self.open = False
    
    def get_door_status(self):
        return self.open
    def get_area(self):
        return self.width * self.height
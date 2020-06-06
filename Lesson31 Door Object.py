# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:11:01 2020

@author: Christopher Cheng
"""

class Door(object):
    def __init__(self):
        self.width = 1
        self.height = 1
        self.open = False
    def change_state(self):
        self.open = not self.open
    def scale(self, factor):
        self.height *= factor
        self.width *= factor
    def get_data(self):
        return [self.width,self.height,self.open]

square_door = Door()
square_door.change_state()
square_door.scale(3)
print(square_door.get_data())
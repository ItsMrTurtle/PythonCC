# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 02:51:39 2020

@author: Christopher Cheng
"""

"""
A game of tag via GUI 
3 Tasks:
    1. Create 2 shapes 
    2. Move them when keys on the keyboard are pressed 
    3. Call a prompt when the 2 shapes touch 
"""

import tkinter
import random

class Player (object):
    def __init__ (self,canvas,color):
        self.color = color
        size = random.randint(50,100)
        x1 = random.randint(100,700) #X-pt for bot left 
        y1 = random.randint(100,700) #y-pt for bot left
        x2 = x1 + size # x pt for top right
        y2 = y1 + size # y pt for top right
        self.coords = [x1 ,y1,x2,y2]
        self.piece = canvas.create_rectangle(self.coords)
        canvas.itemconfig(self.piece, fill = color)
        
    def move(self,direction):
        if direction == "u":
            self.coords[1] -= 10
            self.coords[3] -= 10
            canvas.coords(self.piece, self.coords)
        if direction == "d":
            self.coords[1] += 10
            self.coords[3] += 10
            canvas.coords(self.piece, self.coords)
        if direction == "l":
            self.coords[0] -= 10
            self.coords[2] -= 10
            canvas.coords(self.piece, self.coords)
        if direction == "r":
            self.coords[0] += 10
            self.coords[2] += 10
            canvas.coords(self.piece, self.coords)
        
def handle_key(event):
    if event.char =="w":
        player1.move("u")
    if event.char == "s":
        player1.move("d")
    if event.char == "a":
        player1.move("l")
    if event.char == "d":
        player1.move("r")
    if event.char =="i":
        player2.move("u")
    if event.char == "k":
        player2.move("d")
    if event.char == "j":
        player2.move("l")
    if event.char == "l":
        player2.move("r")
        
    """ Check after each movement if the squares overlap"""
    yellow_xy = canvas.bbox(1) #Gets the coordinates from one of the shapes
    # Returns the ID of any shapes in overlapping
    overlapping = canvas.find_overlapping(yellow_xy[0],yellow_xy[1],\
                                          yellow_xy[2],yellow_xy[3])
    if 2 in overlapping:
        canvas.create_text(100,100, font=("Arial",20), text = "Tag!")
    
""" This section creates a blank window """
window = tkinter.Tk()
window.geometry("800x800")
window.title("Game of Tag")

""" Create a canvas to place the shapes"""
canvas = tkinter.Canvas(window)
canvas.pack(expand=1, fill ="both") # This line rescales the canvas with the window

""" Creates the squares onto the canvas"""
player1 = Player(canvas,"yellow")
player2 = Player(canvas,"blue")

""" Bind the keys via method"""
canvas.bind_all('<Key>', handle_key)

window.mainloop()

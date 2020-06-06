# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:57:28 2020

@author: Christopher Cheng
"""

import tkinter
import random

def changeColors():
    r = random.random()
    if r < 1/3:
        window.configure(background = "red")
        window.update()
    elif 1/3 <= r < 2/3:
        window.configure(background = "green")
        window.update()
    else:
        window.configure(background = "blue")
        window.update()

window = tkinter.Tk()
window.geometry("800x600")
window.title("Color Randomizer Widget")
window.configure(background = "pink")

""" label to instruct the user"""
lbl = tkinter.Label(window, text="Click to change colors!")
lbl.pack()

""" Button that starts the countdown, calls the function when pressed"""
count = tkinter.Button(window, text = "Color Change!", command = changeColors)
count.pack()

window.mainloop()
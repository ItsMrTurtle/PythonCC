# -*- coding: utf-8 -*-
"""
Created on Sat May 30 17:27:01 2020

@author: Christopher Cheng
"""

# Built in GUI library 
import tkinter

def change_color():
    window.configure(background = "White")

# Create a new object to use its properties
window = tkinter.Tk()
window.geometry("800x200")
window.title("My first GUI")
window.configure(background = "grey")

white = tkinter.Button(window, text ="Click", command = change_color)
white.pack()

# Starts the program
window.mainloop()

# -*- coding: utf-8 -*-
"""
Created on Sat May 30 18:19:49 2020

@author: Christopher Cheng
"""
# Built in GUI library 
import tkinter

# Create a new object to use its properties
window = tkinter.Tk()
window.geometry("800x200")
window.title("My first GUI")
window.configure(background = "grey")

red = tkinter.Button(window, text = "Red", bg = "red")
red.pack()

yellow = tkinter.Button(window, text = "yellow", bg = "yellow")
yellow.pack()

green = tkinter.Button(window, text = "green", bg = "green")
green.pack()

# textbox = tkinter.Entry(window)
# textbox.pack()

# colorlabel =tkinter.Label(window, height = "10", width = "10")
# colorlabel.pack()

orange = tkinter.Button(window, text = "Click here", bg = "orange")
orange.pack()

rad1 = tkinter.Radiobutton()
rad2 = tkinter.Radiobutton()
rad1.pack()
rad2.pack()

check = tkinter.Checkbutton()
check.pack()


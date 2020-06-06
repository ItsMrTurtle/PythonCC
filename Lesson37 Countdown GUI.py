# -*- coding: utf-8 -*-
"""
Created on Sat May 30 18:23:58 2020

@author: Christopher Cheng
"""

import tkinter
import time

def countdown():
    countlabel.configure(background = "White")
    """ Get the value from the textbox and change to an int"""
    howlong = int(textbox.get())
    """Make a loop for countdown"""
    for i in range (howlong,0,-1):
        countlabel.configure(text = i) #Change the text
        window.update() #Update the window
        time.sleep(1)
    countlabel.configure(text = "DONE!")
    
""" THis section creates a blank grey blank window """
window = tkinter.Tk()
window.geometry("800x600")
window.title("my first GUI")
window.configure(background = "grey")

""" label to instruct the user"""
lbl = tkinter.Label(window, text="How many seconds to count down?")
lbl.pack()
"""Textbox to enter a number"""
textbox = tkinter.Entry(window)
textbox.pack()
""" Button that starts the countdown, calls the function when pressed"""
count = tkinter.Button(window, text = "Countdown!", command = countdown)
count.pack()
""" A label to print the countdown"""
countlabel = tkinter.Label(window, height = "10", width = "10")
countlabel.pack()

window.mainloop()
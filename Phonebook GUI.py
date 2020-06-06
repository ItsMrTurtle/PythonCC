# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 01:39:51 2020

@author: Christopher Cheng
"""

""" Info in a phonebook like style"""
""" Add and retrive info via GUI"""

import tkinter

class Person(object):
    """
    Stores names, phone numbers, and emails 
    """
    def __init__(self):
        self.name = ""
        self.phone = 1
        self.email = ""
    def set_name(self, name):
        self.name = name
    def set_phone(self,phone):
        self.phone = phone
    def set_email(self,email):
        self.email = email
    def get_name(self):
        return self.name
    def get_phone(self):
        return self.phone
    def get_email(self):
        return self.email
    
def add_contact():
    person = Person()
    name = textbox_name.get()
    phone = textbox_phone.get()
    email = textbox_email.get()
    person.set_name(name)
    person.set_phone(phone)
    person.set_email(email)
    book.append(person)
    label.configure(text = "Contact Added!")

def show_contact():
    clean_string = ""
    for per in book:
        display_name = per.get_name()
        display_number = per.get_phone()
        display_email = per.get_email()
        clean_string += "\n Name: " +display_name + "\n Phone Number: " + \
            display_number + "\n Email: " + display_email + "\n"
    label.configure(text = clean_string)

# Global list var to hold contacts
book = []

""" This section creates a blank window """
window = tkinter.Tk()
window.geometry("800x600")
window.title("Turtle Pages")
window.configure(background = "Yellow")

""" Prompt for name"""
lbl_name = tkinter.Label(window, text="Name")
lbl_name.pack()
"""Textbox to enter a name"""
textbox_name = tkinter.Entry(window)
textbox_name.pack()

""" Prompt for phone number"""
lbl_phone = tkinter.Label(window, text="Phone Number")
lbl_phone.pack()
"""Textbox to enter a phone number"""
textbox_phone = tkinter.Entry(window)
textbox_phone.pack()

""" Prompt for email"""
lbl_email = tkinter.Label(window, text="Email")
lbl_email.pack()
"""Textbox to enter an email"""
textbox_email = tkinter.Entry(window)
textbox_email.pack()

""" Button that adds the contact"""
new_contact = tkinter.Button(window, text = "Add Contact", command = add_contact)
new_contact.pack()

""" Button that shows all contacts"""
all_contact = tkinter.Button(window, text = "Show All Contacts", command = show_contact)
all_contact.pack()

""" A label to print the contacts"""
label = tkinter.Label(window, height = "100", width = "100")
label.configure(background = "white")
label.pack()

window.mainloop()
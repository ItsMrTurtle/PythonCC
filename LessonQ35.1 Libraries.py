# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:21:30 2020

@author: Christopher Cheng
"""


"""
Simulate rolling a die. Show result to user
Show it from compouter side, add a 2s delay, show to user
Ask the user if they want to roll again 
When done playing, show the duration of game in seconds
"""

import random 
import time 

time_start = time.clock()

while True:
    my_roll = random.randint(1,6)
    print("You rolled a",my_roll)
    
    com_roll = random.randint(1,6)
    time.sleep(2) # Add a 2s delay
    print("Com rolled a", com_roll)
    
    if my_roll > com_roll:
        print("You win!")
    elif my_roll < com_roll:
        print("Com wins :(")
    else:
        print("It's a tie")
    
    go = input("Would you like to play again? (yes or no) ")
    if go == "no":
        break

time_end = time.clock()
print("Total time of the game is: ", time_end-time_start, "seconds")
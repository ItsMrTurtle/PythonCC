# -*- coding: utf-8 -*-
"""
Created on Thu May 28 15:49:50 2020

@author: Christopher Cheng
"""

# people = ["Ana","Bob","Carl","Doug","Elle","Finn"]

# # Choice chooses one from a list
# print(random.choice(people))

# # Chooses k amount from a list, no repeats
# print(random.sample(people, 2))

import random
# Simulating a rock paper scissors game 
choice = input("Choose rock, paper, or scissors: ")
# Can set a seed via random.seed(N)
r = random.random()

# [0,1/3) is rock
if r <1/3:
    print("Computer chose rock")
    if choice == "paper":
        print("You win!")
    elif choice == "scissors":
        print("You lose")
    else:
        print("It's a tie")

elif 1/3 <= r < 2/3:
    print("Computer chose paper")
    if choice == "scissors":
        print("You win")
    elif choice == "rock":
        print("You lose")
    else:
        print("It's a tie")

else:
    print("Computer chose scissors")
    if choice =="rock":
        print("You win")
    elif choice == "paper":
        print("you lose")
    else:
        print ("It's a tie")
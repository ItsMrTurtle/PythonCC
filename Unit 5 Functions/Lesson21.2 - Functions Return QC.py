# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:49:13 2020

@author: Christopher Cheng
"""


def guessed_card(number,suit,bet):
    money_won = 0
    guessed = False
    if number == 8 and suit == "hearts":
        money_won = bet * 10
        guessed = True
    else:
        money_won = bet/10
    
    return (guessed, money_won)

# print(guessed_card(8,"hearts",10))
# print(guessed_card("8","hearts",10))
# guessed_card(10,"spades",5)

(did_win,amount) = guessed_card("eight","hearts",80)
print(did_win)
print(amount)
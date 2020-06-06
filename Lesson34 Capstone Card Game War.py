# -*- coding: utf-8 -*-
"""
Created on Wed May 27 18:59:34 2020

@author: Christopher Cheng
"""

"""
Goal: Create a war card type game 
Simplicity: Only use cards 2 to 9, with 4 suits 
Game Rules:
H = hearts, D = diamonds, S = spades, C = clubs (2H/4D/6S/8C)
Player has 2 things: name(str) and hand of cards (list)
Game start: Ask for player names and set them
Each round: Add a card to the player's hands
Compare cards: Number is priority then suit: Spades > Hearts> Diamonds > Clubs
If player has a larger card; remove the card from the winners hand and add \
the card to the losers hand
Once the deck is empty, person with the fewest cards in their hand wins 
"""

class Player(object):
    # Initialize the player's name and start with an empty hand 
    def __init__ (self,name):
        self.name = name
        self.hand = []
    # Return the name of the player if requested
    def get_name(self):
        return self.name
    # Adds a valid card to the hand (adds it to the list)
    def add_card(self,card):
        if card != None:
            self.hand.append(card)
    # Removes a valid card from the hand
    def remove_card(self,card):
        if card != None:
            self.hand.remove(card) # Remove removes the value, pop and del do index
    # Return the number of cards in a hand 
    def get_hand_size(self):
        return len(self.hand)

import random
class CardDeck(object):
    # Initialize the deck of cards the players draw from. When initialized, \
    # it should have all 32 cards from 2-9 with 4 suits each 
    def __init__ (self):
        hearts = "2H,3H,4H,5H,6H,7H,8H,9H"
        spades = "2S,3S,4S,5S,6S,7S,8S,9S"
        diamonds = "2D,3D,4D,5D,6D,7D,8D,9D"
        clubs = "2C,3C,4C,5C,6C,7C,8C,9C"
        # Split via comma and add it into a list 
        self.deck = hearts.split(",") + spades.split(",") \
            + diamonds.split(",") + clubs.split(",")
   
    # Returns 1 random card (str), returns None otherwise
    def get_card(self):
        if len(self.deck) < 1:
             return None
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card
    
    # Compare cards to determine where both drawn cards should go to 
    # First compare num[0], then suits[1]
    def compare_cards(self, card1, card2):
        # Compare numbers in the first 2 ifs
        if card1[0] > card2[0]:
            return card1
        elif card1[0] < card2[0]:
            return card2
        # Compare suits. Since suit order is A-->Z ascending, we can compare them fairly
        elif card1[1] > card2[1]:
            return card1
        else:
            return card2
    
# Initialize the cards and player names
name1 = input("What's your name? Player 1: ")
player1 = Player(name1)
name2 = input("What's your name? Player 2: ")
player2 = Player(name2)
deck = CardDeck()

# Start the game and transactions 
while True:
    player1_card = deck.get_card()
    player2_card = deck.get_card()
    player1.add_card(player1_card)
    player2.add_card(player2_card)
    
    # Stop the game when one person has nothing to pick up 
    if player1_card == None or player2_card == None:
        print("Game Over. No more cards left in the deck.")
        print(name1, "has", player1.get_hand_size())
        print(name2, "has", player2.get_hand_size())
        print("Who won?")
        if player2.get_hand_size() > player1.get_hand_size():
            print(name1, "wins!")
        elif player2.get_hand_size() < player1.get_hand_size():
            print(name2, "wins!")
        else:
            print("Issa tie!") #Same num of cards 
        break #Break to get out of the while loop 
    
    # There are more cards to play around with 
    else:
        print(name1, ":", player1_card)
        print(name2, ":", player2_card)
        if deck.compare_cards(player1_card, player2_card) == player1_card:
            player2.add_card(player1_card)
            player1.remove_card(player1_card)
        else:
            player1.add_card(player2_card)
            player2.remove_card(player2_card)
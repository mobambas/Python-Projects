import random

# Define the suits and ranks for a standard deck of cards
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


# Card class to represent a single playing card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


# Deck class to represent a deck of cards
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        cards_in_deck = ""
        for card in self.deck:
            cards_in_deck = "\n" + cards_in_deck + card.__str__()
        return "Deck has the following cards " + cards_in_deck

    def shuffle(self):
        random.shuffle(self.deck)

    def __len__(self):
        return len(self.deck)


# Player class to represent a player in the card game
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add(self, new_cards):
        self.cards.extend(new_cards)

    def remove(self):
        return self.cards.pop(0)

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        cards_with_player = ""
        for card in self.cards:
            cards_with_player = cards_with_player + "\n" + card.__str__()
        return self.name + " has the following cards " + cards_with_player


# Table class to represent the table in the card game
class Table:
    def __init__(self):
        self.cards = []

    def add(self, new_card):
        self.cards.append(new_card)

    def remove(self):
        self.cards = []

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        table_cards = ""
        for card in self.cards:
            table_cards = "\n" + table_cards + card.__str__()
        return "Table has the following cards " + table_cards


# Function to get player names as input
def player_names():
    player_1 = input("Enter player 1 name: ")
    print("Hi!", player_1)

    player_2 = input("Enter Player 2 name: ")
    print("Hi!", player_2)

    return (player_1, player_2)

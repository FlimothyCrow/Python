import random

class Card :
    def __init__(self, value, operator):
        self.value = value
        self.operator = operator

class Hand :
    def __init__(self, card):
        self.card = card

def makeCard() :
    return Card(random.randint(1, 20), "f")

def makeHand() :
    hand = {}
    for card in range(6) :
        hand[card] = random.randint(1,20)
    return hand


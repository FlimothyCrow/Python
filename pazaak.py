import random

class Card :
    def __init__(self, value, operator):
        self.value = value
        self.operator = operator

class Hand :
    def __init__(self, cards):
        self.cards = cards

def makeCard() :
    operators = {0:"P", 1:"N", 2:"B"}
    return Card(random.randint(1, 20), operators[random.randint(0,2)])

#print(makeCard().operator)

def makeHand() :
    cards = []
    for card in range(3) :
        cards.append(makeCard())
    return Hand(cards)

def sumCards(hand) :
    totalValue = 0
    for card in hand.cards :
        if card.operator == "P" :
            totalValue += card.value
        elif card.operator == "N" :
            totalValue -= card.value
    return totalValue

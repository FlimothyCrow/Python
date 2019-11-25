class Card :
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Hand :
    def __init__(self, Cards):
        self.cards = Cards

def makeCard(string) : # takes a string of value and suit "3C" and makes it into a Card class
    if string[0] == "A" :
        cardValue = 14
    elif string[0] == "K":
        cardValue = 13
    elif string[0] == "Q":
        cardValue = 12
    elif string[0] == "J":
        cardValue = 11
    else :
        cardValue = int(string[:-1])
    return Card(cardValue, string[-1])

def makeHand(cards) : # turns a string of "AS KS QC" into a Hand class
    cardsList = []
    cards = cards.split() # otherwise we'd get " " as it counts every character
    for card in cards :
        cardsList.append(makeCard(card))
    return Hand(cardsList)
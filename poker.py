
'''
hand -> card[0] -> value
                -> suit
     -> card[1] -> value
                -> suit
'''

# DONT EVER PUT LOGIC IN THE CONSTRUCTOR

# NO NOT EVEN THAT KIND


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Hand:
    def __init__(self, Cards):
        self.cards = Cards

def makeCard(cardString) :
    if cardString[0] == "K" :
        cardValue = 13
    elif cardString[0] == "A" :
        cardValue = 14
    elif cardString[0] == "Q":
        cardValue = 12
    elif cardString[0] == "J":
        cardValue = 11
    else :
        cardValue = int(cardString[:-1])
    return Card(cardString[-1], cardValue)

def cardValues(cardString) :
    values = []
    cardString = cardString.split()
    for card in cardString :
        values.append(card[:-1])
    return values

def howManyLike(cardString) :


def matchCheck(cardString) :
    return cardString


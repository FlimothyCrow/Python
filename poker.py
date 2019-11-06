
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
    cardValue = int(cardString[:-1])
    return Card(cardString[-1], cardValue)


class Card :
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Hand :
    def __init__(self, cards):
        self.cards = cards

def makeCard(string) :
    if string[:-1] == "K" :
        cardValue = 13
    elif string[:-1] == "A" :
        cardValue = 14
    elif string[:-1] == "Q":
        cardValue = 12
    elif string[:-1] == "J":
        cardValue = 11
    else :
        cardValue = int(string[:-1])
    return Card(cardValue, string[-1])

def makeHand(string) :
    hand = []
    cards = string.split(" ")
    for card in cards :
        hand.append(makeCard(card))
    return Hand(hand)


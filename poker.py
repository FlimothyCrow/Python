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

def cardValues(hand) :
    valuesList = []
    for card in hand.cards :
        valuesList.append(card.value)
    return valuesList

def pairFinder(hand) :
    values = cardValues(hand)
    pairs = {}
    for value in values :
        if value in pairs :
            pairs[value] += 1
        else :
            pairs[value] = 1
    return pairs

def suitCounter(hand) :
    suits = {}
    for card in hand.cards :
        if card.suit in suits :
            suits[card.suit] += 1
        else :
            suits[card.suit] = 1
    return suits

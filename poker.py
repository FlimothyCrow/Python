
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

class Hand: # add parameter called type
    # def function determineHandType
    # this constructor is a template to make new hands
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

# "factory function" that calls on Hand to create hand instance
def makeHand(cardString) :
    cardsList = []
    cards = cardString.split()
    for card in cards :
        cardsList.append(makeCard(card))
    return Hand(cardsList)

# ========================================
def cardValues(hand) :
    values = []
    for card in hand.cards :
        values.append(card.value)
    return values

def howManyLike(hand) :
    count = {}
    values = cardValues(hand)
    for value in values :
        if value in count :
            count[value] = count[value] + 1
        else :
            count[value] = 1
    return count

def matchCheck(hand) :
    hand = howManyLike(hand).values()
    for value in hand :
        if value == 2 :
            return "pair"
        if value == 3 :
            return "three"
        if value == 4 :
            return "four"

def inOrder(hand) :
    values = cardValues(hand)
    if values[4] - values[0] == 4 :
        return "{} through {}" .format(values[0], values[4])

def highCard(hand) :
    values = cardValues(hand)
    return sorted(values)[-1]

def suitCount(hand) :
    suits = {}
    for card in hand.cards :
        if card.suit in suits:
            suits[card.suit] = suits[card.suit] + 1
        else :
            suits[card.suit] = 1
    if 5 in suits.values() :
        return "flush"

def controller(hand) :
    if matchCheck(hand) :
        return matchCheck(hand)
    elif suitCount(hand) :
        return "flush"
    else :
        return "high card {}" .format(highCard(hand))

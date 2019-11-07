
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
    # def function deteremineHandType
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
    cardString = howManyLike(hand)
#    if
    return cardString


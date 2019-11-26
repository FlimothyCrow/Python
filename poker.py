class Card :
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Hand :
    def __init__(self, cards):
        self.cards = cards
        """self.card1 = card1
        self.card2 = card2
        self.card3 = card3
        self.card4 = card4"""


def makeCard(string) :
    if string[0] == "A" :
        cardValue = 14
    elif string[0] == "K" :
        cardValue = 13
    elif string[0] == "Q" :
        cardValue = 12
    elif string[0] == "J" :
        cardValue = 11
    else :
        cardValue = int(string[:-1])
    return Card(cardValue, string[-1])

def makeHand(stringOfCards) :
    cards = []
    for card in stringOfCards.split(" ") :
        cards.append(card)
    return Hand(cards)

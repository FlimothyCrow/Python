import random

class Card :
    def __init__(self, value, operator):
        self.value = value
        self.operator = operator

    def cardValue(self):
        if self.operator == "P" :
            return self.value
        elif self.operator == "N" :
            return -self.value

class Hand :
    def __init__(self, cards):
        self.cards = cards

def makeCard() :
    operators = {0:"P", 1:"N", 2:"B"}
    return Card(random.randint(1, 20), operators[random.randint(0,2)])

#print(makeCard().operator)
# add functions (easily testable) into a class for high cohesion, low coupling

def makeHand() :
    cards = []
    for card in range(3) :
        cards.append(makeCard())
    return Hand(cards)

def sumCards(hand) :
    totalValue = 0
    for card in hand.cards :
        totalValue += card.cardValue()
    return totalValue

def aiCard(hand, total) :
    sortedCards = sorted(hand.cards, key=lambda x: x.value, reverse=True)
    reverseSortCards = sorted(hand.cards, key=lambda x: x.value)
    if total < 20 :
        for card in sortedCards :
            if card.cardValue() + total <= 20 :
                return card
    else :
        for card in reverseSortCards :
            if card.cardValue() + total <= 20 :
                return card

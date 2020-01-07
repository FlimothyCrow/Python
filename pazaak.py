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
    if total == 20 :
       return None
    sortedCards = sorted(hand.cards, key=lambda x: x.cardValue(), reverse=True)
    for card in sortedCards :
        if card.cardValue() + total <= 20 :
            del hand.cards[0]
            return card
# draw, play or stay

def playGame(hand, drawDeck) :
    total = 0
    while total < 15 :
        total += drawDeck[0]
        del drawDeck[0]
    card = aiCard(hand, total)
    if card:
        total += card.cardValue()
    return total

def gameController(hand, drawDeck) :
    total = 0
    AI = 0
    Player = 0
    tie = 0
    for turn in range(3) :
        total = playGame(hand, drawDeck)
        if total == 20 :
            return "AI wins"
        elif total > 20 :
            return "wings of pastrami"
        else :
            return "humanity wins"

# story 1 - make controller that plays 3 rounds of game and returns win count
#           is given a longer "draw deck"

# story 2 - run a manual simulation on controller with a real random draw deck and same hand and
#           several different numbers for the 15 card limit and see which
#           number provides the highest average totals below 20  (optionally play two ais against each other
#           with differnt numbers passed in for the "15" amount and see which wins most)

# story 3 - make aicard choose positive or negative MIND BLOWN
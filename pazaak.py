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
        elif self.operator == "B" :
            return -self.value

class Hand :
    def __init__(self, cards):
        self.cards = cards

class Scoreboard :
    def __init__(self, ai, player, tie):
        self.ai = ai
        self.player = player
        self.tie = tie

#print(makeCard().operator)
# add functions (easily testable) into a class for high cohesion, low coupling

def makeCard() :
    operators = {0:"P", 1:"N", 2:"B"}
    return Card(random.randint(1, 10), operators[random.randint(0,2)])

def deckGenerator() :
    deck = []
    for card in range(29) :
        deck.append(random.randint(1,10))
    return deck

def makeHand() :
    cards = []
    for card in range(3) :
        cards.append(makeCard())
    return Hand(cards)

def handPrinter() :
    handList = []
    hand = makeHand()
    for card in hand.cards :
        handList.append(card.operator)
    return handList

#for hand in range(99999) : # this print test is returning correct numerical values!
#    print(handPrinter()) # it also returns correct ranges of ["B", "P", "N"]

def boardMaker(ai, player, tie) :
    return Scoreboard(ai, player, tie)

def sumCards(hand) :
    totalValue = 0
    for card in hand.cards :
        totalValue += card.cardValue()
    return totalValue

def aiCard(hand, total) :
    if total == 20 :
       return None
    if hand :
        sortedCards = sorted(hand.cards, key=lambda x: x.cardValue(), reverse=True)
        if len(sortedCards) > 0 :
            for card in sortedCards :
                if 16 < card.cardValue() + total <= 20 :
                    del hand.cards[0]
                    return card
    else :
        return None
# draw, play or stay

def playGame(hand, drawDeck):
    total = 0
    while total < 16:
        total += drawDeck[0]
        del drawDeck[0]
        card = aiCard(hand, total)
        if card:
            total += card.cardValue()
        elif not hand :
            total += drawDeck[0]
            del drawDeck[0]
    return total

def gameController(hand, drawDeck, turns) :
    total = 0
    ai = 0
    player = 0
    tie = 0
    for turn in range(turns) :
        total = playGame(hand, drawDeck)
        if 17 < total < 21 :
            ai += 1
        elif total > 20 :
            player += 1
        else :
            tie += 1
    return boardMaker(ai, player, tie)

def manualRun(turns) :
    listOfResults = []
    randomHand = makeHand()
    randomDrawDeck = deckGenerator()
    #randomHand = Hand([Card(5, "P"), Card(2, "N"), Card(10, "N"), Card(4, "B")])
    #randomDrawDeck = [1, 2, 9, 10, 5]
    listOfResults.append(gameController(randomHand, randomDrawDeck, turns))
    return listOfResults

#print(manualRun(1)[0].ai)

# the print works with pre-defined hand and deck
# two successful tests with randoms, and then :
# TypeError: '<' not supported between instances of 'NoneType' and 'int' on line 55
# sorting by calling cardValue on line 66 based on positive or negative is causing the problem
# sortedCards can't handle the "B" conditional!
# changed "B" to "P" on line 29
# need to incorporate .cardValue function on line 8


# story 1 - make controller that plays 3 rounds of game and returns win count
#           is given a longer "draw deck"

# story 2 - run a manual simulation on controller with a real random draw deck and same hand and
#           several different numbers for the 15 card limit and see which
#           number provides the highest average totals below 20  (optionally play two ais against each other
#           with different numbers passed in for the "15" amount and see which wins most)

# story 3 - make aicard choose positive or negative MIND BLOWN



class Card :
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Hand :
    def __init__(self, cards):
        self.cards = cards

class RankedHand :
    def __init__(self, rank, tiebreaker):
        self.rank = rank
        self.tiebreaker = tiebreaker

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

def keyReturn(dictionary, targetValue) :
    for key, value in dictionary.items():
        if targetValue == value:
            return key

def pairReturn(hand) :
    matches = pairFinder(hand)
    twoCounter = 0
    for card in hand.cards :
        if card.value == 2 :
            twoCounter += 1
    if 2 in matches.values() and 3 in matches.values():
        return "full house"
    elif twoCounter == 2 :
        return "two pair"
    elif 2 in matches.values() :
        return "pair {}".format()
    elif 3 in matches.values() :
        return "three"
    elif 4 in matches.values() :
        return "four"

def suitCounter(hand) :
    suits = {}
    for card in hand.cards :
        if card.suit in suits :
            suits[card.suit] += 1
        else :
            suits[card.suit] = 1
    return suits

def checkStraight(hand) :
    values = cardValues(hand)
    lowestValue = min(values)
    highestValue = max(values)
    if highestValue - lowestValue == 4 :
        return "straight {} through {}".format(lowestValue, highestValue)

def highCard(hand) :
    values = cardValues(hand)
    return max(values)

def controller(hand) :
    if pairReturn(hand) :
        return pairReturn(hand)
    elif checkStraight(hand) and 5 in suitCounter(hand).values() :
        return "straight flush"
    elif checkStraight(hand) :
        return checkStraight(hand)
    elif 5 in suitCounter(hand).values() :
        return "flush"
    else :
        return highCard(hand)

#def handRank(hand) :
    #handType = controller(hand)
    #return RankedHand()
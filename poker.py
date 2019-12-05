from enum import Enum

class Card :
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Hand :
    def __init__(self, cards):
        self.cards = cards

class RankedHand :
    def __init__(self, rank, tiebreaker): # fudge tiebreaker as integer for suit strength
        self.rank = rank
        self.tiebreaker = tiebreaker

class RankList(Enum) :
    HC = 1
    Pair = 2
    TwoPair = 3
    Three = 4
    ST = 5
    Flush = 6
    FH = 7
    Four = 8
    SF = 9

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

def findDuplicates(matchesDict) :
    pairs = {}
    for key in matchesDict :
        if matchesDict[key] == 2 :
            pairs[key] = 2
    return pairs

def pairReturn(hand) :
    dup = findDuplicates(pairFinder(hand))
    matches = pairFinder(hand)
    twoCounter = 0
    for card in dup :
        if dup[card] == 2 :
            twoCounter += 1
    if 2 in matches.values() and 3 in matches.values():
        return RankedHand(RankList.FH, keyReturn(matches, 3))
    elif twoCounter == 2 :
        return RankedHand(RankList.TwoPair, next(iter(dup)))
    elif 2 in matches.values() :
        return RankedHand(RankList.Pair, keyReturn(matches, 2))
    elif 3 in matches.values() :
        return RankedHand(RankList.Three, keyReturn(matches, 3))
    elif 4 in matches.values() :
        return RankedHand(RankList.Four, keyReturn(matches, 4))

def suitCounter(hand) :
    suits = {}
    for card in hand.cards :
        if card.suit in suits :
            suits[card.suit] += 1
        else :
            suits[card.suit] = 1
    if 5 in suits.values() :
        return RankedHand(RankList.Flush, next(iter(suits)))

def checkStraight(hand) :
    values = cardValues(hand)
    lowestValue = min(values)
    highestValue = max(values)
    if highestValue - lowestValue == 4 :
        return RankedHand(RankList.ST, int(highestValue))

def highCard(hand) :
    values = cardValues(hand)
    return RankedHand(RankList.HC, max(values))

def rankHand(hand) :
    if pairReturn(hand) :
        return pairReturn(hand)
    elif checkStraight(hand) and suitCounter(hand) :
        return RankedHand(RankList.SF, checkStraight(hand).tiebreaker)
    elif checkStraight(hand) :
        return checkStraight(hand)
    elif suitCounter(hand) :
        return suitCounter(hand)
    else :
        return highCard(hand)

def compareHands(handObject0, handObject1) :
    rankedHand0 = rankHand(handObject0)
    rankedHand1 = rankHand(handObject1)
    if rankedHand0.rank.value == rankedHand1.rank.value :
        if rankedHand0.tiebreaker > rankedHand1.tiebreaker :
            return "Player 1 wins"
        elif rankedHand1.tiebreaker < rankedHand0.tiebreaker :
            return "Player 2 wins"
        elif rankedHand0.tiebreaker == rankedHand1.tiebreaker :
            if highCard(handObject0).tiebreaker > highCard(handObject1).tiebreaker :
                return "Player 1 wins"
            else :
                return "Player 2 wins"
    elif rankedHand0.rank.value > rankedHand1.rank.value :
        return "Player 1 wins"
    else :
        return "Player 2 wins"
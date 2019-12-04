from enum import Enum

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
    pairs = []
    for key in matchesDict.keys() :
        if matchesDict[key] == 2 :
            pairs.append(key)
    return pairs

def pairReturn(hand) :
    dup = findDuplicates(pairFinder(hand))
    matches = pairFinder(hand)
    twoCounter = 0
    for card in hand.cards :
        if card.value == 2 :
            twoCounter += 1
    if 2 in matches.values() and 3 in matches.values():
        return RankedHand(RankList.FH, keyReturn(matches, 3))
    elif twoCounter == 2 :
        return RankedHand(RankList.TwoPair, dup[1])
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

def controller(hand) :
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

def handRank(hand) :
    handType = controller(hand)
    split = handType.split(" ")
    if "straight flush" in handType :
        return RankedHand(split[0], split[1])
    elif "straight" in handType :
        return RankedHand(split[0], split[-1])
    else :
        return RankedHand(split[0], split[1])

#create class enumeration to equate strings and integers
#rebuild pairReturn, checkStraight and highCard with enum
#remove string manipulation from controller and merge with handRank
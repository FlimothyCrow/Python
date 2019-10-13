
def cardValueList(hand) :
    return list(map(cardValue, hand.split()))

def checkFrequency(cardvalues) :
    counts = {}
    for cardvalue in cardvalues:
        if cardvalue in counts:
            counts[cardvalue] = counts[cardvalue] + 1
        else:
            counts[cardvalue] = 1
    return counts

def highCard(hand) :
    cards = hand.split()
    currentHigh = cards[0]
    for card in cards :
        if cardValue(card) > cardValue(currentHigh) :
            currentHigh = card
    return currentHigh

def cardValue(card) :
    if card[0] == "K" :
        return 13
    if card[0] == "J" :
        return 11
    if card[0] == "Q" :
        return 12
    if card[0] == "A" :
        return 14
    if card[1] == "0" :
        return 10
    else :
        return int(card[0])

# FOR DOESN'T WORK ON DICTIONARIES
# ITEMS CONVERTS INTO A LIST (PROB OF TUPLES)
def pairCheck(hand) :
    values = cardValueList(hand)
    freqDict = checkFrequency(values)
    for card,count in freqDict.items() :
        if (2 in (dict.values(freqDict))) and (3 in (dict.values(freqDict))) :
            return "full house", max(freqDict.keys()), min(freqDict.keys())
        if count == 2 :
            return "pair of {}" .format(card)
        if count == 3 :
            return "three of a kind {}" .format(card)
        if count == 4 :
            return "four of a kind {}" .format(card)

def orderCheck(hand) :
    newList = sorted(cardValueList(hand))
    if newList[4] - newList[0] == 4 :
        return "straight {} through {}" .format(newList[0], newList[4])

def getSuit(card) :
    return card[-1]

def suitList(hand) :
    suits = checkFrequency(map(getSuit, hand.split()))
    for suit,count in suits.items():
        if count == 5:
            return suit

def pokerHands(hand) :
    if suitList(hand) : #straight flush
        if orderCheck(hand) :
            return orderCheck(hand),suitList(hand)
    if suitList(hand) : #flush
        return suitList(hand)
    if pairCheck(hand) : #2, 3 or 4 of a kind, full house
        return pairCheck(hand)
    if orderCheck(hand): #straight
        return orderCheck(hand)
    else :
        return "high card", highCard(hand)


    



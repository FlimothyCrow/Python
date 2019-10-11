
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

def pairCheck(hand) :
    values = cardValueList(hand)
    for card,count in checkFrequency(values).items() :
        if count == 2 :
            return card

def orderCheck(hand) :
    newList = sorted(cardValueList(hand))
    if newList[4] - newList[0] == 4 :
        return True

def getSuit(card) :
    return card[-1]

def suitList(hand) :
    suits = checkFrequency(map(getSuit, hand.split()))
    for suit,count in suits.items():
        if count == 5:
            return suit

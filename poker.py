class Card :
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Hand :
    def __init__(self, cards):
        self.cards = cards


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
        cards.append(makeCard(card))
    return Hand(cards)


def cardValues(hand) :
    values = []
    for card in hand.cards :
        values.append(card.value)
    return values


def matchCounter(hand) :
    cardsDict = {}
    for value in cardValues(hand) :
        if value not in cardsDict.keys() :
            cardsDict.update({value : 1})
        else :
            cardsDict[value] += 1
    return cardsDict


def suitCounter(hand) :
    suitsDict = {}
    for card in hand.cards :
        if card.suit not in suitsDict :
            suitsDict.update({card.suit : 1})
        else :
            suitsDict[card.suit] += 1
    return suitsDict


def isStraight(hand) :
    smallest = int(min(cardValues(hand)))
    largest = int(max(cardValues(hand)))
    if largest - smallest == 4 :
        return "Straight {} through {}".format(smallest, largest)
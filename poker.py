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


def cardCounter(hand) :
    cardsDict = {}
    for value in cardValues(hand) :
        if value not in cardsDict.keys() :
            cardsDict.update({value : 1})
        else :
            cardsDict[value] += 1
    return cardsDict


def matchReturn(hand) :
    values = cardCounter(hand).values()
    for card in values :
        if 2 in values and 3 in values :
            return "full house"
        if card == 2 :
            return "pair"
        elif card == 3 :
            return "three"
        elif card == 4 :
            return "four"


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


def highCard(hand) :
    values = cardValues(hand)
    return max(values)


def controller(hand) :
    if 5 in suitCounter(hand).values() :
        return "flush"
    elif matchReturn(hand) :
        return matchReturn(hand)
    elif isStraight(hand) :
        return isStraight(hand)
    else :
        return highCard(hand)


def printer() :
    cards = input("Choose five cards")
    hand = makeHand(cards)
    print(controller(hand))

printer()
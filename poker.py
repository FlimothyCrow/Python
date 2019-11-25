class Card :
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

def makeCard(string) :
    if string[0] == "A" :
        cardValue = 14
    if string[0] == "K":
        cardValue = 13
    if string[0] == "Q":
        cardValue = 12
    if string[0] == "J":
        cardValue = 11
    else :
        cardValue = int(string[:-1])
    return Card(cardValue, string[-1])
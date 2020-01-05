import random


def chooseCard() :
    cards = {1:1, 2:2, 3:3, 4:-4}
    return cards[(random.randint(1, 4))]

def makeHand() :
    hand = {}
    for card in range(5) :
        hand[card] = random.randint(1,20)
    return hand

print(makeHand())
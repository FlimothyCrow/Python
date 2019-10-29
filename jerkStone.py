import random
# health counter for both players
# mana counter for both players
# any card does hero damage for its mana cost
# bleeding out is a factor, but it's a constant (1 per turn)
# there are dud cards (0 mana, no effect)
# max hand size is 5 cards, the next draw is discarded
# each deck has 20 damage cards
# we don't need to define each deck, just have a counter for total number
# then just pull a random card and put it into defined "hand"

# mutating variables for each player's health


# def playCard(cardCost, damage)
     # player2Health = player2Health - damage
     # player1Mana = player1Mana - cardCost

def cardGenerator() :
    return random.randint(1, 11)

def startDeck() :
    deck = []
    for i in range(21) :
        drawCard(deck, cardGenerator())
    return deck

def drawCard(playerHand, card) :
    playerHand.append(card)
    return playerHand

def playCard(playerHand, card) :
    playerHand.remove(card)
    return playerHand

def dealDamage(playerHealth, damage) :
    if playerHealth - damage > 0:
        return playerHealth - damage
    else :
        return None



#def gamePlay() :


#gamePlay()
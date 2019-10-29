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
#

# def playCard(cardCost, damage)
     # player2Health = player2Health - damage
     # player1Mana = player1Mana - cardCost

def cardGenerator() :
    return random.randint(1, 11)

def startDeck() :
    deck = []
    for i in range(18) :
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

def gamePlay() :
    playerHand = [1, 2, 3]
    mana = 10
    enemyHealth = 30
    playerDeck = (startDeck())
    drawCard(playerHand, playerDeck[0]) # this copies random card from pD -> pH
    playerDeck.pop(0)
    print("Your current hand is:\n", playerHand, "\nYou have {} cards left in your deck" .format(len(playerDeck)))
    print("The enemy's health is currently {}".format(enemyHealth))
    playedCard = input("Which card would you like to play?")
    if int(playedCard) <= mana :
        mana = mana - int(playedCard)
        print("You played {}".format(playedCard))
        enemyHealth = dealDamage(enemyHealth, playedCard)
        print("You did {} damage to the enemy".format(playedCard))
        print("You now have {} mana remaining" .format(mana))
    else :
        print("You don't have enough mana for that card, ya mook, try again")
        print("You now have {} mana remaining".format(mana))
    print("You can play another card or you can end your turn")



gamePlay()
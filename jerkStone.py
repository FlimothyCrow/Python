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

gameState = {'health': 30,
             'mana': 10,
             'hand':[1, 2, 3],
             'deck':[3, 5, 7, 4, 3, 5, 8, 9, 9, 10, 10, 1, 2, 1]}


def cardGenerator() :
    return random.randint(1, 11)

#def startDeck() :


def drawCard(state) :
    deck = state.get('deck')
    hand = state.get('hand')
    hand.append(deck[0])
    del deck[0]
    return state

def playCard(state, card) :
    deck = state.get('deck')
    if card in deck :
        deck.remove(card)
    return state

def dealDamage(state, damage) :
    damagePoints = (state.get('health')) - damage
    state.update({'health': damagePoints})
    return state

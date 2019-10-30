import random

gameState = {'health': 30,
             'mana': 10,
             'hand':[1, 2, 3],
             'deck':[3, 5, 7, 4, 3, 5, 8, 9, 9, 10, 10, 1, 2, 1]}

def cardGenerator() :
    return random.randint(1, 11)

#def startDeck(state) :

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

import random

gameState = {'health': 30,
             'mana': 0,
             'hand':[1, 2, 3],
             }

def cardGenerator() :
    return random.randint(1, 11)

def startDeck(state) :
    drawnCards = []
    state["deck"] = drawnCards
    for i in range(18) :
        drawnCards.append(cardGenerator())
    return state

def drawCard(state) :
    deck = state.get('deck')
    hand = state.get('hand')
    if len(hand) >= 5 :
        del deck[0]
        return state
    else:
        hand.append(deck[0])
        del deck[0]
        return state

def playCard(state, card) :
    spent = state.get('mana') - card
    hand = state.get('hand')
    if card in hand :
        if state.get('mana') >= card :
            hand.remove(card)
            state.update({'mana': spent})
        else :
            return "mana"
    else :
        return "card"
    return state

def dealDamage(state, damage) :
    damagePoints = (state.get('health')) - damage
    state.update({'health': damagePoints})
    return state

def statePrinter(state) :
    print(" Health {}\n".format(state.get('health')),
          "Mana {}\n" .format(state.get('mana')),
          "Cards {}\n".format(state.get('hand')))
statePrinter(gameState)

#'{0} in {1}'.format(unicode(self.author, 'utf-8'), unicode(self.publication, 'utf-8'))

"""
controller jobs
define current player
startDeck
loop
    mana + 1
    drawCard
    playCard
    dealDamage
    end turn
    switch player
/loop
"""
#def stateController(state) :
#    startDeck(state)



#stateController(gameState)


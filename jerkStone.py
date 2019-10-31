import random

gameState = {'health': 30,
             'mana': 1,
             'hand':[1, 2, 3],
             'turn':1,
             }

gameState2 = {'health': 30,
             'mana': 1,
             'hand':[1, 2, 3],
             'turn': 1,
             'deck':[0, 5]}

def cardGenerator() :
    return random.randint(1, 11)

def startDeck(state) :
    drawnCards = []
    state["deck"] = drawnCards
    for i in range(7) :
        drawnCards.append(cardGenerator())
    return state

def drawCard(state) :
    deck = state.get('deck')
    hand = state.get('hand')
    if state['mana'] < 10 :
        state['mana'] = state['mana'] + 1
    else :
        state['mana'] = state['mana']
    if len(hand) >= 5 :
        del deck[0]
        return state
    else:
        hand.append(deck[0])
        del deck[0]
        return state

def validPlay(state, card) :
    if int(card) <= int(state['mana']) :
        if card in state['hand'] :
            return True

def dealDamage(state, damage) :
    damagePoints = (state.get('health')) - damage
    state.update({'health': damagePoints})
    return state

def statePrinter(state) :
    print(" Health {}\n".format(state.get('health')),
          "Mana {}\n" .format(state.get('mana')),
          "Cards {}\n".format(state.get('hand')),
          "There are {} cards left in your deck".format(len(state.get('deck'))))

def endTurn(state) :
    health = state['health']
    state = drawCard(state)
    state = restoreMana(state)
    if not state['deck']:
        state.update({'health': health - 1})
    return state

def restoreMana(state) :
    state['mana'] = state['turn']
    return state

def playCard(state, card) :
    spent = state.get('mana') - int(card)
    hand = state.get('hand')
    if validPlay(state, card) :
        hand.remove(int(card))
        state.update({'mana': spent})
        state = dealDamage(state, int(card))

    return state

def stateController2(state) :
    turnCount = state['turn']
    state = startDeck(state)
    while True :
        turnCount = turnCount + 1
        statePrinter(state)
        nextPlay = input("Pick a card")
        if nextPlay == "END" :
            state = endTurn(state)
        else:
            state = playCard(state, nextPlay)

# the board is only printed with endTurn, not on playCard
# when the loop ends, drawCard is called but playCard is not
# input("END") causes invalid literal for in() with base 10
# ONE LOOP ONE PRINT ONE INPUT
# ghost recon

#turnCounter in gameState
# add counter in endTurn
#stateController2(gameState)


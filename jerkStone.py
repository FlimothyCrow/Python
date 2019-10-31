import random

gameState = {'health': 30,
             'mana': 1,
             'hand':[1, 2, 3],
             }

gameState2 = {'health': 30,
             'mana': 1,
             'hand':[1, 2, 3],
             'deck': [0, 5]}

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

def playCard(state, card) :

    spent = state.get('mana') - int(card)
    hand = state.get('hand')
    hand.remove(int(card))
    state.update({'mana': spent})
    state = dealDamage(state, int(card))
    return state

def dealDamage(state, damage) :
    damagePoints = (state.get('health')) - damage
    state.update({'health': damagePoints})
    return state

def statePrinter(state) :
    print(" Health {}\n".format(state.get('health')),
          "Mana {}\n" .format(state.get('mana')),
          "Cards {}\n".format(state.get('hand')),
          "There are {} cards left in your deck".format(len(state.get('deck'))))

def validPlay(state, card) :
    if int(card) <= int(state['mana']) :
        if card in state['hand'] :
            return True
        else :
            return "card"
    else :
        return "mana"
# add AI health and decks in gameState
#statePrinter(gameState2)

def endTurn(state) :
    state = drawCard(state)
    #state = restoreMana(state)
    # bleeding damage if deck == zero
    return state

def restoreMana(state, turnCounter) :
    state['mana'] = turnCounter
    return state

def stateController2(state) :
    state = startDeck(state)
    counter = 0
    while True :
        counter = counter + 1
        statePrinter(state)
        nextPlay = input("Pick a card")
        if nextPlay == "END" :
            state = endTurn(state) # restore mana, draw card,
        else:
                state = playCard(state, nextPlay)
                # if health == zero - > break

# ONE LOOP ONE PRINT ONE INPUT
# deal Damage attacks "player health"
# update tests for dealDamage
# valid play within playCard to return None, maybe add a "why turn failed" in endGame
# build restoreMana
# bleeding damage if deck == zero

#stateController2(gameState)

# ghost recon
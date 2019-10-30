import random

gameState = {'health': 30,
             'mana': 0,
             'hand':[1, 2, 3],
             }

gameState2 = {'health': 30,
             'mana': 0,
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
    spent = state.get('mana') - card
    hand = state.get('hand')
    hand.remove(card)
    state.update({'mana': spent})
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
    if card <= int(state['mana']) :
        if card in state['hand'] :
            return True
        else :
            return "card"
    else :
        return "mana"

#statePrinter(gameState2)

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
def stateController(state) :
    deckState = startDeck(state)
    deckState = drawCard(deckState)
    statePrinter(deckState)
    firstCard = input("It's your turn. You can play a card or end your turn")
    if playCard(deckState, int(firstCard)) :


        """
        print("You don't have enough mana to play that card")
    elif playCard(deckState, int(firstCard)) == "card" :
        print("You don't have that card in your hand")
    else:
        deckState = playCard(deckState, int(firstCard))
        """
    statePrinter(deckState)
    #nextCard = input("You can play another card, or type 'END' to end your turn")

#assign new variable to each return

#stateController(gameState)

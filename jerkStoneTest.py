import unittest
from jerkStone import *


class jerkStoneTest(unittest.TestCase):

    def test_drawCard(self):
        newGameState = {'health': 30,
                     'mana': 10,
                     'hand': [1, 2, 3],
                     'deck': [4, 5, 7, 4, 3, 5, 8, 9, 9, 10, 10, 1, 2, 1]}

        tooManyCards = {'health': 30,
                     'mana': 10,
                     'hand': [1, 2, 3, 8, 9],
                     'deck': [0, 1, 2]}

        self.assertEqual({'health': 30,
                 'mana': 10,
                 'hand': [1, 2, 3, 4],
                 'deck': [5, 7, 4, 3, 5, 8, 9, 9, 10, 10, 1, 2, 1]}, drawCard(newGameState))

        self.assertEqual({'health': 30,
                'mana': 10,
                'hand': [1, 2, 3, 8, 9],
                'deck': [1, 2]}, drawCard(tooManyCards))

    #def test_startDeck(self):
        #self.assertEqual([1], startDeck())

    def test_playCard(self):
        newGameState = {'health': 30,
                        'mana': 2,
                        'hand': [1, 2, 3],
                        'deck': [3, 5]}

        self.assertEqual({'health': 30,
                        'mana': 1,
                        'hand': [2, 3],
                        'deck': [3, 5]}, playCard(newGameState, 1))

        self.assertEqual(None, playCard(newGameState, 3))




    def test_dealDamage(self):
        self.assertEqual({'health': 25,
                 'mana': 10,
                 'hand': [1, 2, 3],
                 'deck': [3, 5, 7, 4, 3, 5, 8, 9, 9, 10, 10, 1, 2, 1]}, dealDamage(gameState, 5))

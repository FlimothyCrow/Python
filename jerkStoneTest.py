import unittest
from jerkStone import *


class jerkStoneTest(unittest.TestCase):

    def test_drawCard(self):
        newGameState = {'health': 30,
                     'mana': 10,
                     'hand': [1, 2, 3],
                     'deck': [3, 5, 7, 4, 3, 5, 8, 9, 9, 10, 10, 1, 2, 1]}

        self.assertEqual({'health': 30,
                 'mana': 10,
                 'hand': [1, 2, 3, 3],
                 'deck': [5, 7, 4, 3, 5, 8, 9, 9, 10, 10, 1, 2, 1]}, drawCard(newGameState))

    #def test_startDeck(self):
        #self.assertEqual([1], startDeck())

    def test_playCard(self):
        newGameState = {'health': 30,
                        'mana': 10,
                        'hand': [1, 2, 3],
                        'deck': [3, 5, 7, 4, 3, 5, 8, 9, 9, 10, 10, 1, 2, 1]}

        self.assertEqual({'health': 30,
                        'mana': 10,
                        'hand': [1, 2, 3],
                        'deck': [3, 7, 4, 3, 5, 8, 9, 9, 10, 10, 1, 2, 1]}, playCard(newGameState, 5))


    def test_dealDamage(self):
        self.assertEqual({'health': 25,
                 'mana': 10,
                 'hand': [1, 2, 3],
                 'deck': [3, 5, 7, 4, 3, 5, 8, 9, 9, 10, 10, 1, 2, 1]}, dealDamage(gameState, 5))

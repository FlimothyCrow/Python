import unittest
from jerkStone import *


class jerkStoneTest(unittest.TestCase):

    gameState = {'health': 30,
                 'mana': 10,
                 'hand': [1, 2, 3],
                 'deck': [3, 5, 7, 4, 3, 5, 8, 9, 9, 10, 10, 1, 2, 1]}


    def test_drawCard(self):
        self.assertEqual([1, 3, 5], drawCard([1, 3], 5))

    def test_startDeck(self):
        self.assertEqual([1], startDeck())

    def test_playCard(self):
        self.assertEqual([3, 5, 2, 1], playCard([3, 5, 2, 1, 7], 7))
        self.assertEqual([3, 3, 5, 8, 5, 2, 1, 7, 7], playCard([7, 3, 3, 5, 8, 5, 2, 1, 7, 7], 7))

    def test_dealDamage(self):
        self.assertEqual({'health': 25,
                 'mana': 10,
                 'hand': [1, 2, 3],
                 'deck': [3, 5, 7, 4, 3, 5, 8, 9, 9, 10, 10, 1, 2, 1]}, dealDamage(gameState, 5))
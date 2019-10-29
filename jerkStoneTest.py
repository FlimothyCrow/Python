import unittest
from jerkStone import *


class jerkStoneTest(unittest.TestCase):


    def test_drawCard(self):
        self.assertEqual([1, 3, 5], [1, 2, 3, 4], drawCard([1, 3], [1, 2, 3, 4, 5], 5))

    def test_startDeck(self):
        self.assertEqual([1], startDeck())

    def test_playCard(self):
        self.assertEqual([3, 5, 2, 1], playCard([3, 5, 2, 1, 7], 7))
        self.assertEqual([3, 3, 5, 8, 5, 2, 1, 7, 7], playCard([7, 3, 3, 5, 8, 5, 2, 1, 7, 7], 7))

    def test_dealDamage(self):
        self.assertEqual(20, dealDamage(25, 5))
        self.assertEqual(None, dealDamage(3, 7))
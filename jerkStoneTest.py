import unittest
from jerkStone import *


class jerkStoneTest(unittest.TestCase):


    def test_drawCard(self):
        self.assertEqual([1, 2, 9], drawCard([1, 2], 9))

    def test_startDeck(self):
        self.assertEqual([1], startDeck())

    def test_playCard(self):
        self.assertEqual([3, 5, 2, 1], playCard([3, 5, 2, 1, 7], 7))
        self.assertEqual([3, 3, 5, 8, 5, 2, 1, 7, 7], playCard([7, 3, 3, 5, 8, 5, 2, 1, 7, 7], 7))
import unittest
from jerkStone import *


class jerkStoneTest(unittest.TestCase):


    def test_drawCard(self):
        self.assertEqual([1, 2, 9], drawCard([1, 2], 9))

    def test_startDeck(self):
        self.assertEqual([1], startDeck())
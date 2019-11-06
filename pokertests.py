import unittest
from poker import *


class PokerTests(unittest.TestCase):

    def test_makeCard(self):
        card = makeCard("6S")
        card0 = makeCard("KD")
        self.assertEqual(6, card.value)
        self.assertEqual("S", card.suit)
        self.assertEqual("D", card0.suit)

'''
    def test_makeHand(self):
        hand = makeHand("KS KS KS KS KS")
        self.assertEqual(13, hand.cards[0].value)
        self.assertEqual("S", hand.cards[0].suit)
'''
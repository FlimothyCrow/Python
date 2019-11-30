import unittest
from poker import *


class PokerTests(unittest.TestCase):

    def test_makeCard(self):
        card = makeCard("KD")
        self.assertEqual(13, card.value)

    def test_makeCard1(self):
        card = makeCard("AD")
        self.assertEqual(14, card.value)

    def test_makeCard2(self):
        card = makeCard("KD")
        self.assertEqual("D", card.suit)
##########
    def test_makeHand0(self):
        hand = makeHand("3D 5C KD QS 10D")
        self.assertEqual(10, hand.cards[4].value)

    def test_makeHand1(self):
        hand = makeHand("3D 5C KD QS 10D")
        self.assertEqual("C", hand.cards[1].suit)
import unittest
from poker import *


class PokerTests(unittest.TestCase):

    def test_makeCard(self):
        card = makeCard("6S")
        self.assertEqual(6, card.value)

        card0 = makeCard("10C")
        self.assertEqual(10, card0.value)

        card1 = makeCard("QH")
        self.assertEqual(12, card1.value)

    def test_makeHand(self):
        hand = makeHand("AS KS KS JC 6S")
        self.assertEqual(14, hand.cards[0].value)
        self.assertEqual(6, hand.cards[4].value)
        self.assertEqual(11, hand.cards[3].value)
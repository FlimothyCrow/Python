import unittest
from poker import *


class PokerTests(unittest.TestCase):

    def test_makeCard(self):
        card = makeCard("6S")
        card0 = makeCard("KD")
        self.assertEqual(6, card.value)
        self.assertEqual("S", card.suit)
        self.assertEqual("D", card0.suit)
        self.assertEqual(13, card0.value)

    def test_matchCheck(self):
        self.assertEqual("pair", matchCheck(makeHand("3S 3D QD 5H 8C")))

    def test_howManyLike(self):
        self.assertEqual({3: 2, 9: 1, 14: 1, 13: 1}, howManyLike(makeHand("AD KS 3D 9H 3C")))

    def test_cardValues(self):
        self.assertEqual([14, 13, 10, 9, 3], cardValues(makeHand("AD KS 10C 9H 3C")))

    def test_makeHand(self):
        hand = makeHand("KS KS KS KS KS")
        self.assertEqual(13, hand.cards[0].value)
        self.assertEqual("S", hand.cards[0].suit)

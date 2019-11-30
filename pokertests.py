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
##########
    def test_cardValues(self):
        hand = makeHand("3C 4D 9H 9D AS")
        actual = cardValues(hand)
        self.assertEqual([3, 4, 9, 9, 14], actual)
##########
    def test_pairFinder(self):
        hand = makeHand("3C 9H 9C 2S KC")
        actual = pairFinder(hand)
        self.assertEqual({3: 1, 9: 2, 13: 1, 2: 1}, actual)
##########
    def test_suitCounter(self):
        hand = makeHand("3C 9C 8C KC JC")
        actual = suitCounter(hand)
        self.assertEqual({"C": 5}, actual)
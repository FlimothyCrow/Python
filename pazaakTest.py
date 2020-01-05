import unittest
from pazaak import *


class pazaakTest(unittest.TestCase):

    def test_cardValue(self):
        card = Card(5, "P")
        self.assertEqual(5, card.cardValue())

    def test_cardValue2(self):
        card = Card(2, "N")
        self.assertEqual(-2, card.cardValue())

    def test_sumCards(self):
        hand = Hand([Card(3, "P"), Card(2, "P")])
        self.assertEqual(5, sumCards(hand))

    def test_sumCards2(self):
        hand = Hand([Card(3, "N"), Card(6, "P"), Card(1, "P")])
        self.assertEqual(4, sumCards(hand))

    def test_aiCard(self):
        hand = Hand([Card(1, "P"), Card(2, "P"), Card(3, "P"), Card(5, "P")])
        self.assertEqual(hand.cards[2], aiCard(hand, 16))

    def test_aiCard2(self):
        hand = Hand([Card(8, "P"), Card(2, "P"), Card(3, "P"), Card(5, "P")])
        self.assertEqual(None, aiCard(hand, 19))

    def test_aiCard3(self):
        hand = Hand([Card(1, "P"), Card(2, "P"), Card(4, "P"), Card(5, "P")])
        self.assertEqual(hand.cards[2], aiCard(hand, 16))

    def test_aiCard4(self):
        hand = Hand([Card(1, "P"), Card(2, "N"), Card(4, "P"), Card(5, "P")])
        self.assertEqual(hand.cards[1], aiCard(hand, 21))

    def test_aiCard5(self):
        hand = Hand([Card(1, "P"), Card(4, "N"), Card(3, "N"), Card(5, "P")])
        self.assertEqual(hand.cards[2], aiCard(hand, 23))

    def test_aiCard6(self):
        hand = Hand([Card(2, "P"), Card(3, "N")])
        self.assertEqual(hand.cards[1], aiCard(hand, 21))
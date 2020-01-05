import unittest
from pazaak import *


class pazaakTest(unittest.TestCase):
    def test_makeCard(self):
        card = makeCard()
        self.assertEqual("f", card.operator) # this passes without the randint generators

    def test_makeHand(self):
        hand = makeHand()
        self.assertEqual("P", hand.cards[0].operator)

    def test_sumCards(self):
        hand = Hand([Card(3, "P"), Card(2, "P")])
        self.assertEqual(5, sumCards(hand))

    def test_sumCards2(self):
        hand = Hand([Card(3, "N"), Card(6, "P"), Card(1, "P")])
        self.assertEqual(4, sumCards(hand))
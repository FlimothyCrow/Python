import unittest
from poker import *


class PokerTests(unittest.TestCase):

    def test_makeCard(self):
        card = makeCard("6S")
        self.assertEqual(6, card.value)

        card = makeCard("KS")
        self.assertEqual(13, card.value)

        card = makeCard("QD")
        self.assertEqual(12, card.value)

        card = makeCard("AC")
        self.assertEqual(14, card.value)

        card = makeCard("JS")
        self.assertEqual(11, card.value)
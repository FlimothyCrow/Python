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
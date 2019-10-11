import unittest
from poker import *


class PokerTests(unittest.TestCase):
    def test_cardValue(self):
        self.assertEqual(13, cardValue("KD"))
        self.assertEqual(11, cardValue("JS"))
        self.assertEqual(12, cardValue("QS"))
        self.assertEqual(14, cardValue("AC"))
        self.assertEqual(5, cardValue("5H"))
        self.assertEqual(10, cardValue("10H"))

    def test_highCard(self):
        self.assertEqual("4D", highCard("3H 2D 4D"))
        self.assertEqual("KD", highCard("3H KD 2D 4D"))
        self.assertEqual("5S", highCard("3H 5S 2D 4D"))
        self.assertEqual("10C", highCard("3S 9H 10C 7S 6D"))

    def test_pairCheck(self):
        self.assertEqual(4, pairCheck("4H 9S KC 4D AS"))
        self.assertEqual(None, pairCheck("3H 9S KC 4D AS"))

    def test_checkFrequency(self):
        self.assertEqual({4:3, 9:1}, checkFrequency([4,9,4, 4]))

    def test_orderCheck(self):
        self.assertEqual(True, orderCheck("2D 3S 4C 5S 6H"))
        self.assertEqual(True, orderCheck("JS AD KC QH 10S"))
        self.assertEqual(None, orderCheck("JS AD KC QH 9S"))

    def test_cardValueCheck(self):
        self.assertEqual([2, 3, 4, 5, 6], cardValueList("2D 3S 4C 5S 6H"))

    def test_suitList(self):
        self.assertEqual("H", suitList("8H AH 3H JH KH"))
        self.assertEqual(None, suitList("8H AH 3S JH KH"))
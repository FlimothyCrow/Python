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
        self.assertEqual("pair of 4", pairCheck("4H 9S KC 4D AS"))
        self.assertEqual(None, pairCheck("3H 9S KC 4D AS"))
        self.assertEqual("three of a kind 8", pairCheck("8H 8S C 8D AS"))
        self.assertEqual("four of a kind 13", pairCheck("KS KD KC KH 4C"))

    def test_checkFrequency(self):
        self.assertEqual({4:3, 9:1}, checkFrequency([4,9,4, 4]))

    def test_orderCheck(self):
        self.assertEqual("straight 2 through 6", orderCheck("2D 3S 4C 5S 6H"))
        self.assertEqual("straight 10 through 14", orderCheck("JS AD KC QH 10S"))
        self.assertEqual(None, orderCheck("JS AD KC QH 9S"))

    def test_cardValueCheck(self):
        self.assertEqual([2, 3, 4, 5, 6], cardValueList("2D 3S 4C 5S 6H"))

    def test_suitList(self):
        self.assertEqual("H", suitList("8H AH 3H JH KH"))
        self.assertEqual(None, suitList("8H AH 3S JH KH"))

    def test_pokerHands(self):
        self.assertEqual("straight 3 through 7", pokerHands("3D 4C 5S 6H 7C"))
        self.assertEqual("pair of 10", pokerHands("10D 10C 8S KC AH"))
        self.assertEqual("H", pokerHands("3H AH QH 7H 6H"))
        self.assertEqual("S", pokerHands("3S AS QS 7S 6S"))
        self.assertEqual("three of a kind 8", pokerHands("8S 8C 8D 2D 3S"))
        self.assertEqual("four of a kind 9", pokerHands("9S 9C 9D 2D 9S"))
        self.assertEqual("straight flush", pokerHands("3H 4H 5H 7H 6H"))

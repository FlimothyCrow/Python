import unittest
from poker import *


class PokerTests(unittest.TestCase):

    def test_makeCard(self):
        card = makeCard("6S")
        card0 = makeCard("KD")
        card1 = makeCard("3C")
        self.assertEqual(6, card.value)
        self.assertEqual("S", card.suit)
        self.assertEqual("D", card0.suit)
        self.assertEqual(13, card0.value)
        self.assertEqual("C", card1.suit)
        self.assertEqual(3, card1.value)

    def test_howManyLike(self):
        self.assertEqual({3: 2, 9: 1, 14: 1, 13: 1}, howManyLike(makeHand("AD KS 3D 9H 3C")))

    def test_cardValues(self):
        self.assertEqual([14, 13, 10, 9, 3], cardValues(makeHand("AD KS 10C 9H 3C")))

    def test_makeHand(self):
        hand = makeHand("KS KS KS KS KS")
        self.assertEqual(13, hand.cards[0].value)
        self.assertEqual("S", hand.cards[0].suit)

    def test_matchCheck(self):
        self.assertEqual("pair", matchCheck(makeHand("3S 3D QD 5H 8C")))
        self.assertEqual("three", matchCheck(makeHand("3S 3D QD 3H 8C")))
        self.assertEqual("four", matchCheck(makeHand("3S 3D QD 3H 3C")))
        self.assertEqual("full house", matchCheck(makeHand("3S 3D QD 3H QC")))

    def test_inOrder(self):
        self.assertEqual("2 through 6", inOrder(makeHand("2D 3C 4H 5H 6D")))
        self.assertEqual("10 through 14", inOrder(makeHand("10C JD QD KS AC")))

    def test_suitCount(self):
        #self.assertEqual({"D": 2, "C": 2, "H": 1}, suitCount((makeHand("AD 3C 4D KC 6H"))))
        self.assertEqual("flush", suitCount((makeHand("AD 3D 4D KD 6D"))))

    def test_highCard(self):
        self.assertEqual(12, highCard((makeHand("3D QD 2S 5H 7C"))))

    def test_controller(self):
        self.assertEqual("high card 9", controller(makeHand("3D 2S 8H 9H 5S")))
        self.assertEqual("pair", controller(makeHand("5D 2S 8H 9H 5S")))
        self.assertEqual("three", controller(makeHand("5D 2S 5H 9H 5S")))
        self.assertEqual("four", controller(makeHand("5D 5C 5H 9H 5S")))
        self.assertEqual("flush", controller(makeHand("3D AD 9D 4D KD")))
        self.assertEqual("straight flush", controller(makeHand("2D 3D 4D 5D 6D")))
        self.assertEqual("straight", controller(makeHand("2D 3D 3C 5D 6D")))
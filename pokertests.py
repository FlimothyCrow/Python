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
    def test_keyReturn(self):
        matches = {14: 1, 10: 2, 3: 1}
        self.assertEqual(10, keyReturn(matches, 2))
##########
    def test_findDuplicates(self):
        hand = makeHand("9H 9S QC QS 2D")
        matches = pairFinder(hand)
        actual = findDuplicates(matches)
        self.assertEqual([9, 12], actual)
##########
    def test_pairReturn(self):
        hand = makeHand("3C 9H 9C 2S KC")
        actual = pairReturn(hand)
        self.assertEqual("pair 9", actual)

    def test_pairReturn1(self):
        hand = makeHand("9C 9H 9C 2S KC")
        actual = pairReturn(hand)
        self.assertEqual("three 9", actual)

    def test_pairReturn2(self):
        hand = makeHand("AD AS AC AH KC")
        actual = pairReturn(hand)
        self.assertEqual("four 14", actual)

    def test_pairReturn4(self):
        hand = makeHand("2C 9H 9C 2S 9C")
        actual = pairReturn(hand)
        self.assertEqual("full house 2 9", actual)

    def test_pairReturn3(self):
        hand = makeHand("2C 9H 9C 2S KC")
        actual = pairReturn(hand)
        self.assertEqual("two pair 2 9", actual)
##########
    def test_suitCounter(self):
        hand = makeHand("3C 9C 8C KC JC")
        actual = suitCounter(hand)
        self.assertEqual({"C": 5}, actual)
##########
    def test_highCard(self):
        hand = makeHand("3C 9C 2S 4H KS")
        actual = highCard(hand)
        self.assertEqual(13, actual)
##########
    def test_checkStraight(self):
        hand = makeHand("7C 8H 9S 10H JS")
        actual = checkStraight(hand)
        self.assertEqual("straight 7 through 11", actual)
##########
    def test_controller(self):
        hand = makeHand("3C 3S 9D 8C QH")
        actual = controller(hand)
        self.assertEqual("pair 3", actual)

    def test_controller1(self):
        hand = makeHand("3C 4C 9C 8C QC")
        actual = controller(hand)
        self.assertEqual("flush C", actual)

    def test_controller3(self):
        hand = makeHand("3C 4C 5C 6C 7H")
        actual = controller(hand)
        self.assertEqual("straight 3 through 7", actual)

    def test_controller4(self):
        hand = makeHand("3C 4C 5C 6C 7C")
        actual = controller(hand)
        self.assertEqual("straight flush", actual)

    def test_controller5(self):
        hand = makeHand("3C 4C 5C 6C QS")
        actual = controller(hand)
        self.assertEqual(12, actual)
##########
    def test_handRank(self):
        hand = makeHand("3H 3C 5H 9S QD")
        actual = handRank(hand)
        self.assertEqual("pair", actual.rank)
        self.assertEqual("3", actual.tiebreaker)

    def test_handRank1(self):
        hand = makeHand("6C 7D 8S 9H 10D")
        actual = handRank(hand)
        self.assertEqual("straight", actual.rank)
        self.assertEqual("10", actual.tiebreaker)

    def test_handRank2(self):
        hand = makeHand("10S JS QS KS AS")
        actual = handRank(hand)
        self.assertEqual("straight", actual.rank)
        self.assertEqual("flush", actual.tiebreaker)


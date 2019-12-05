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
        #hand = makeHand("9H 9S QC QS 2D")
        matches = {9: 2, 12: 2, 2: 1}
        actual = findDuplicates(matches)
        self.assertEqual({9: 2, 12: 2}, actual)
##########
    def test_pairReturn(self):
        hand = makeHand("3C 9H 9C 2S KC")
        actual = pairReturn(hand)
        self.assertEqual(9, actual.tiebreaker)
        self.assertEqual(RankList.Pair, actual.rank)

    def test_pairReturn1(self):
        hand = makeHand("9C 9H 9C 2S KC")
        actual = pairReturn(hand)
        self.assertEqual(9, actual.tiebreaker)
        self.assertEqual(RankList.Three, actual.rank)

    def test_pairReturn2(self):
        hand = makeHand("AD AS AC AH KC")
        actual = pairReturn(hand)
        self.assertEqual(14, actual.tiebreaker)
        self.assertEqual(RankList.Four, actual.rank)

    def test_pairReturn4(self):
        hand = makeHand("2C 9H 9C 2S 9C")
        actual = pairReturn(hand)
        self.assertEqual(9, actual.tiebreaker)
        self.assertEqual(RankList.FH, actual.rank)

    def test_pairReturn3(self):
        hand = Hand([Card(9, "C"), Card(4, "S"), Card(9, "H"), Card(4, "C"), Card(14, "S")])
        actual = pairReturn(hand)
        self.assertEqual(9, actual.tiebreaker)
        self.assertEqual(RankList.TwoPair, actual.rank)
# manually construct a class to discern which function is failing
# now we now that pairReturn is the failure, not makeHand
# we've eliminated findDuplicates as the cause

    def test_pairReturn5(self):
        hand = makeHand("3C 5S 3D 5C QH")
        actual = pairReturn(hand)
        self.assertEqual(RankList.TwoPair, actual.rank)

##########
    def test_suitCounter(self):
        hand = makeHand("3C 9C 8C KC JC")
        actual = suitCounter(hand)
        self.assertEqual("C", actual.tiebreaker)
        self.assertEqual(RankList.Flush, actual.rank)

##########
    def test_highCard(self):
        hand = makeHand("3C 9C 2S 4H KS")
        actual = highCard(hand)
        self.assertEqual(13, actual.tiebreaker)
        self.assertEqual(RankList.HC, actual.rank)

##########
    def test_checkStraight(self):
        hand = makeHand("7C 8H 9S 10H JS")
        actual = checkStraight(hand)
        self.assertEqual(RankList.ST, actual.rank)
        self.assertEqual(11, actual.tiebreaker)
##########
    def test_controller(self):
        hand = makeHand("3C 3S 9D 8C QH")
        actual = controller(hand)
        self.assertEqual(3, actual.tiebreaker)
        self.assertEqual(RankList.Pair, actual.rank)

    def test_controller1(self):
        hand = makeHand("3C 4C 9C 8C QC")
        actual = controller(hand)
        self.assertEqual(RankList.Flush, actual.rank)
        self.assertEqual("C", actual.tiebreaker)

    def test_controller3(self):
        hand = makeHand("3C 4C 5C 6C 7H")
        actual = controller(hand)
        self.assertEqual(7, actual.tiebreaker)
        self.assertEqual(RankList.ST, actual.rank)

    def test_controller4(self):
        hand = makeHand("3C 4C 5C 6C 7C")
        actual = controller(hand)
        self.assertEqual(RankList.SF, actual.rank)
        self.assertEqual(7, actual.tiebreaker)

    def test_controller5(self):
        hand = makeHand("3C 4C 5C 6C QS")
        actual = controller(hand)
        self.assertEqual(12, actual.tiebreaker)

    def test_controller6(self):
        hand = makeHand("3C 3D 3S 6C 6S")
        actual = controller(hand)
        self.assertEqual(RankList.FH, actual.rank)
##########
    def test_compareHands(self):
        hand0 = makeHand("3C 3D 9S 8H AC")
        hand1 = makeHand("9D 9C 9S AH QS")
        actual = compareHands(hand0, hand1)
        self.assertEqual("Player 2 wins", actual)

    def test_compareHands1(self):
        hand0 = makeHand("3C 3D 3S 3H AC")
        hand1 = makeHand("9D 9C 9S AH QS")
        actual = compareHands(hand0, hand1)
        self.assertEqual("Player 1 wins", actual)
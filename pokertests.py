import unittest
from poker import *


class PokerTests(unittest.TestCase):

    def test_makeCard(self):
        card = makeCard("6S")
        self.assertEqual(6, card.value)
        ###########
        card = makeCard("KS")
        self.assertEqual(13, card.value)

        card = makeCard("QD")
        self.assertEqual(12, card.value)

        card = makeCard("AC")
        self.assertEqual(14, card.value)

        card = makeCard("JS")
        self.assertEqual(11, card.value)
        self.assertEqual("S", card.suit)

    ###########
    def test_makeHand(self):
        hand = makeHand("KS 3D 5H 9H KD")
        self.assertEqual(13, hand.cards[0].value)
        self.assertEqual("S", hand.cards[0].suit)
        self.assertEqual(9, hand.cards[3].value)

    ###########
    def test_cardValues(self):
# arrange NO LOGIC, PRIMITIVES ONLY OR CONSTRUCTORS (THEY HAVE NO LOGIC)
        hand = Hand([Card(13, "S"), Card(14, "D"), Card(3, "D"), Card(13, "C")])
# act ONLY CALL THE FUNCTION TO BE TESTED
        actual = cardValues(hand)
# assert NO LOGIC
        self.assertEqual([13, 14, 3, 13], actual)

    ###########
    def test_cardCounter0(self):
        hand = Hand([Card(13, "S"), Card(14, "D"), Card(3, "D"), Card(13, "C")])
        self.assertEqual({13: 2, 14: 1, 3: 1}, cardCounter(hand))

    def test_cardCounter1(self):
        hand = Hand([Card(3, "S"), Card(3, "D"), Card(3, "C"), Card(14, "S")])
        self.assertEqual({3: 3, 14 : 1}, cardCounter(hand))

    def test_cardCounter2(self):
        hand = Hand([Card(5, "S"), Card(5, "D"), Card(5, "C"), Card(5, "S")])
        self.assertEqual({5: 4}, cardCounter(hand))
    ###########
    def test_matchReturn0(self):
        hand = Hand([Card(13, "C"), Card(3, "S"), Card(2, "S"), Card(13, "S")])
        actual = matchReturn(hand)
        self.assertEqual("pair", actual)

    def test_matchReturn1(self):
        hand = Hand([Card(3, "C"), Card(3, "S"), Card(2, "S"), Card(3, "S")])
        actual = matchReturn(hand)
        self.assertEqual("three", actual)

    def test_matchReturn2(self):
        hand = Hand([Card(5, "C"), Card(5, "H"), Card(5, "D"), Card(5, "S")])
        actual = matchReturn(hand)
        self.assertEqual("four", actual)

    """def test_matchReturn3(self):
        hand = Hand([Card(5, "C"), Card(5, "H"), Card(2, "D"), Card(2, "S"), Card(2, "C")])
        actual = matchReturn(hand)
        self.assertEqual("full house", actual)"""

    ###########
    def test_suitCounter1(self):
        hand = Hand([Card(10, "C"), Card(2, "C"), Card(4, "D"), Card(5, "D")])
        self.assertEqual({"C": 2, "D": 2}, suitCounter(hand))

    def test_suitCounter2(self):
        hand = Hand([Card(13, "C"), Card(3, "S"), Card(2, "S"), Card(13, "S")])
        self.assertEqual({"S": 3, "C": 1}, suitCounter(hand))

    ###########
    def test_isStraight0(self):
        hand = Hand([Card(2, "S"), Card(4, "C"), Card(3, "C"), Card(6, "D"), Card(5, "H")])
        actual = isStraight(hand)
        self.assertEqual("Straight 2 through 6", actual)

    def test_isStraight1(self):
        hand = Hand([Card(10, "S"), Card(14, "C"), Card(11, "C"), Card(13, "D"), Card(11, "H")])
        actual = isStraight(hand)
        self.assertEqual("Straight 10 through 14", actual)
    ###########
    def test_highCard(self):
        hand = Hand([Card(10, "S"), Card(14, "C"), Card(9, "C"), Card(13, "D"), Card(11, "H")])
        actual = highCard(hand)
        self.assertEqual(14, actual)
    ###########
    def test_controller(self):
        hand = Hand([Card(10, "S"), Card(10, "C"), Card(11, "C"), Card(13, "D"), Card(5, "H")])
        actual = controller(hand)
        self.assertEqual("pair", actual)
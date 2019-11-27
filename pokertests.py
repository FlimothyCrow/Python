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
        self.assertEqual("S", card.suit)

    def test_makeHand(self):
        hand = makeHand("KS 3D 5H 9H KD")
        self.assertEqual(13, hand.cards[0].value)
        self.assertEqual("S", hand.cards[0].suit)
        self.assertEqual(9, hand.cards[3].value)


    def test_cardValues(self):
# arrange NO LOGIC, PRIMITIVES ONLY OR CONSTRUCTORS (THEY HAVE NO LOGIC)
        hand = Hand([Card(13, "S"), Card(14, "D"), Card(3, "D"), Card(13, "C")])
# act ONLY CALL THE FUNCTION TO BE TESTED
        actual = cardValues(hand)
# assert NO LOGIC
        self.assertEqual([13, 14, 3, 13], actual)

    def test_matchCounter(self):
        hand = Hand([Card(13, "S"), Card(14, "D"), Card(3, "D"), Card(13, "C")])
        self.assertEqual({13: 2, 14: 1, 3: 1}, matchCounter(hand))
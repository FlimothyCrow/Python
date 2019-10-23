import unittest
from fizzBuzz import *


class PokerTests(unittest.TestCase):
    def test_listRange(self):
        self.assertEqual([1,2], listRange(1, 3))

    def test_wordNums(self):
        self.assertEqual([1, 2, "Jerk", 4], wordChanger([1, 2, 3, 4], 3, "Jerk"))
        self.assertEqual(["schmo", 4, 5, "schmo"], wordChanger([3, 4, 5, 6], 3, "schmo"))
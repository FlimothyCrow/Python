import unittest
from fizzBuzz import *


class fizzBuzz(unittest.TestCase):
    def test_wordChanger(self):
        self.assertEqual([1, 2, "Jerk", 4], wordChanger([1, 2, 3, 4], 3, "Jerk"))
        self.assertEqual([1, 2, "Jerk", 4, 5, "Jerk"], wordChanger([1, 2, 3, 4, 5, 6], 3, "Jerk"))
        self.assertEqual([1, 2, "Jerk", 4, 5, "eyy"], wordChanger([1, 2, "Jerk", 4, 5, 6], 3, "eyy"))

    def test_listRange(self):
        self.assertEqual([1, 2, 3, 4, 5], listRange(1, 6))
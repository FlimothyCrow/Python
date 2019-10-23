import unittest
from fizzBuzz import *


class fizzBuzz(unittest.TestCase):

    def test_wordChanger(self):
        self.assertEqual([1, 2, "Jerk", 4], wordChanger([1, 2, 3, 4], 3, "Jerk"))
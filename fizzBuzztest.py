import unittest
from fizzBuzz import *


class fizzBuzz(unittest.TestCase):

    jerks = [1, 2, 3, 4, 5, 6, 7]

    def test_wordChanger(self):
        jerks = [1, 2, 3, 4, 5, 6]
        self.assertEqual([1, 2, 1, 4, 5, 1], wordChanger(jerks, 3, 1))
        self.assertEqual([1, 2, "jerks", 4, 5, "jerks"], wordChanger(jerks, 3, "jerks"))

    def test_listRange(self):
        self.assertEqual([1, 2, 3, 4, 5], listRange(1, 6))
import unittest
from fizzBuzz import *


class PokerTests(unittest.TestCase):
    def test_listRange(self):
        self.assertEqual([1,2], listRange(1, 3))


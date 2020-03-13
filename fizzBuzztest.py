import unittest
from fizzBuzz import *


class fizzBuzz(unittest.TestCase):

    def test_fizzBuzz(self):
        jerks = [1, 2, 3, 4, 5, 6]
        parsedList = fizzBuzz(jerks)
        self.assertEqual([3, 6], parsedList)


import unittest
from fizzBuzz import *


class fizzBuzz(unittest.TestCase):

    def test_mockCase(self):
        cased = mockCase("sandwich")
        self.assertEqual("sAnDwIcH", cased)

    def test_sortByValue(self):
        arrayOfObjects = [["A", 3], ]
        cased = sortByValue(5, 10)
        self.assertEqual(15, cased)


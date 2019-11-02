import unittest
from mergeSort import *


class mergeSortTest(unittest.TestCase):

    def test_wordChanger(self):
        self.assertEqual([1, 2, 3, 4, 5], sortNumerical([5, 3, 4, 1, 2]))

import unittest
from mergeSort import *


class mergeSortTest(unittest.TestCase):

    def test_wordChanger(self):
        self.assertEqual([1, 2, 3, 4, 5], sortNumerical([5, 3, 4, 1, 2]))
        self.assertEqual([[1, 2], [1,3], [4, 0]], sortNumerical([[4,0], [1,2], [1,3]]))

    def test_sortReverse(self):
        self.assertEqual([5, 4, 3, 2, 1], sortReverse([3, 4, 1, 5, 2]))


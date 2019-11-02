import unittest
from mergeSort import *


class mergeSortTest(unittest.TestCase):

    def test_sortNumerical(self):
        self.assertEqual([1, 2, 3, 4, 5], sortNumerical([5, 3, 4, 1, 2]))
        self.assertEqual([[1, 2], [1,3], [4, 0]], sortNumerical([[4,0], [1,2], [1,3]]))
        self.assertEqual(['integer', 'lingonberry', 'pancake', 'schlamazzle', 'set'], sortNumerical(["integer", "set", "pancake", "lingonberry", "schlamazzle"]))

    def test_sortReverse(self):
        self.assertEqual([5, 4, 3, 2, 1], sortReverse([3, 4, 1, 5, 2]))
        self.assertEqual([[3,0], [1,0], [0,3], [0,1]], sortReverse([[1,0], [3,0], [0,3], [0,1]]))
        self.assertEqual([[0, 1], [0, 0, 1], [0, 0, 0, 1]], sortReverse([[0, 1], [0, 0, 1], [0, 0, 0, 1]]))
        #self.assertEqual(["x", "b", "a", 3, 1], sortReverse([1, "a", 9, "x", 3, "b"]))
        self.assertEqual(["jerk store", "every time I die", "alphabet", "Curly's a dope"], sortReverse(["alphabet", "jerk store", "every time I die", "Curly's a dope"]))
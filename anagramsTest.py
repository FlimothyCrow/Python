import unittest
from anagrams import *


def test_anagrams(self):
    list0 = [1, "c", 3, 4, 2, 6, "238", 238, "sick liaisons"]
    list1 = [1, 3, "c", 2, 4, 6, "238", "sick liaisons", 238]
    self.assertEqual(True, anagrams(list0, list1))


def test_anagrams1(self):
    list0 = [1, "c", 3, 4, 2, 6, 238, 238, "sick liaisons"]
    list1 = [1, 3, "c", 2, 4, 6, "238", "sick liaisons", 238]
    self.assertEqual(False, anagrams(list0, list1))


def test_anagrams2(self):
    list0 = [1, "c", 3, 4, 2, 6, 238, "sick liaisons"]
    list1 = [1, 3, "c", 2, 4, 6, "238", "sick liaisons", 238]
    self.assertEqual(False, anagrams(list0, list1))

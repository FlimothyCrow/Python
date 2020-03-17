import unittest
from managrams import *

class managramsTest(unittest.TestCase):

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

    def test_fizzBuzz(self):
        listToParse = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual([1, 2, "fizz", "buzz", 5, "fizz", 7, "buzz", "fizz"], fizzBuzz(listToParse))


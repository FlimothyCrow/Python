import unittest
from banking import *


class bankingTest(unittest.TestCase):


    def test_parseEntries(self):
        inputTwo = ("    _  _     _  _  _  _  _ \n"+
                    "  | _| _||_||_ |_   ||_||_|\n"+
                    "  ||_  _|  | _||_|  ||_| _|\n"+
                    "                           \n"+
                    " _ \n"+
                    "| |\n"+
                    "|_|\n"+
                    "   ")

        self.assertEqual(1, parseEntries(0, 0, inputTwo))
        self.assertEqual(2, parseEntries(0, 1, inputTwo))
        self.assertEqual(3, parseEntries(0, 2, inputTwo))
        self.assertEqual(4, parseEntries(0, 3, inputTwo))
        self.assertEqual(5, parseEntries(0, 4, inputTwo))
        self.assertEqual(6, parseEntries(0, 5, inputTwo))
        self.assertEqual(7, parseEntries(0, 6, inputTwo))
        self.assertEqual(8, parseEntries(0, 7, inputTwo))
        self.assertEqual(9, parseEntries(0, 8, inputTwo))
        self.assertEqual(0, parseEntries(1, 0, inputTwo))
        #print(inputTwo)

    def test_entryValidator(self):
        self.assertEqual(None, entryValidator([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.assertEqual(None, entryValidator([1, 2, 3, 4, 5, 6, 7, 9]))

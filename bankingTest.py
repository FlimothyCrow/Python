import unittest
from banking import *


class bankingTest(unittest.TestCase):


    def test_parseEntries(self):
        inputTwo = ("    _  _     _  _  _  _  _ \n"+
                    "  | _| _||_||_ |_   ||_||_|\n"+
                    "  ||_  _|  | _||_|  ||_| _|\n"+
                    "\n"+
                    " _ \n"+
                    "| |\n"+
                    "|_|\n"+
                    "\n")

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
        self.assertEqual(True, entryValidator([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.assertEqual(None, entryValidator([6, 6, 4, 3, 7, 1, 4, 9, 5]))

    def test_accountNumbers(self):
        account = ("    _  _     _  _  _  _  _ \n"+
                   "  | _| _||_||_ |_   ||_||_|\n"+
                   "  ||_  _|  | _||_|  ||_| _|\n"+
                   "\n"+
                   "    _  _  _  _  _  _     _ \n"+
                   "|_||_|| || ||_   |  |  ||_ \n"+
                   "  | _||_||_||_|  |  |  | _|\n"+
                   "\n")

        self.assertEqual("123456789", accountNumbers(account, 0))
        self.assertEqual("490067715 error message", accountNumbers(account, 1))

    #def test_accountPrinter(self):
        #self.assertEqual("123456789", accountPrinter(account))
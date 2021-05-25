import unittest
from renameUtility import *


class fizzBuzz(unittest.TestCase):

    def test_filterString0(self):
        parsed = filterString("  things [].txt", "file")
        self.assertEqual("things .txt", parsed)

    def test_filterString1(self):
        parsed = filterString("]][ - .   jerk.jpg", "file")
        self.assertEqual("jerk.jpg", parsed)

    def test_filterString2(self):
        parsed = filterString("testFolder[[[[[", "folder")
        self.assertEqual("testFolder", parsed)


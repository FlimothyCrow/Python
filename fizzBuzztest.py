import unittest
from fizzBuzz import *


class fizzBuzz(unittest.TestCase):

    def test_mockCase(self):
        cased = mockCase("sandwich")
        self.assertEqual("sAnDwIcH", cased)


import unittest
from insultGenerator import *


class insultGeneratorTest(unittest.TestCase):

    def test_randomNumber(self):
        self.assertEqual(1, randomNumber())

    def test_parseInsult(self):
        self.assertEqual(["a", "b"], parseInsult(0, "a, b\nc, d\n, e, f"))
        self.assertEqual(["c", "d"], parseInsult(1, "a, b\nc, d\n, e, f"))
        self.assertEqual(["e", "f"], parseInsult(2, "a, b\nc, d\n, e, f"))
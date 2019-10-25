import unittest
from insultGenerator import *


class insultGeneratorTest(unittest.TestCase):


    def test_parseInsult(self):
        self.assertEqual(["a", "b"], parseInsult(0, "a, b\nc, d\ne, f"))
        self.assertEqual(["c", "d"], parseInsult(1, "a, b\nc, d\ne, f"))
        self.assertEqual(["e", "f"], parseInsult(2, "a, b\nc, d\ne, f"))
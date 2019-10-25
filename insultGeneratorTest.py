import unittest
from insultGenerator import *


class insultGeneratorTest(unittest.TestCase):

    def test_randomNumber(self):
        self.assertEqual(1, randomNumber())

import unittest
from insultGenerator import *


class insultGeneratorTest(unittest.TestCase):


    def test_parseInsult(self):
        self.assertEqual("dumb", jerk("dumb"))

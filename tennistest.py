import unittest
from tennis import *


class tennistest(unittest.TestCase):

    def test_tennis(self):
        self.assertEqual("fifteen love", tennis(1,0))
        self.assertEqual("fifteen thirty", tennis(1,2))
        self.assertEqual("forty thirty", tennis(3, 2))
        self.assertEqual("love forty", tennis(0, 3))

    def test_score(self):
        self.assertEqual("love", score(0))
        self.assertEqual("fifteen", score(1))
        self.assertEqual("thirty", score(2))
        self.assertEqual("forty", score(3))

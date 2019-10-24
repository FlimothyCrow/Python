import unittest
from tennis import *


class tennistest(unittest.TestCase):

    def test_tennis(self):
        self.assertEqual("fifteen love", tennis(1,0))
        self.assertEqual("fifteen thirty", tennis(1,2))
        self.assertEqual("forty thirty", tennis(3, 2))
        self.assertEqual("love forty", tennis(0, 3))
        self.assertEqual("deuce", tennis(3, 3))


    def test_score(self):
        self.assertEqual("love", score(0))
        self.assertEqual("fifteen", score(1))
        self.assertEqual("thirty", score(2))
        self.assertEqual("forty", score(3))

    def test_victory(self):
        self.assertEqual(True, victory(4, 2))
        self.assertEqual(None, victory(3, 1))
        self.assertEqual(None, victory(6, 7))
        self.assertEqual(None, victory(1, 0))

    def test_whoWins(self):
        self.assertEqual("player 1", whoWins(1, 0))
        self.assertEqual("player 2", whoWins(1, 3))

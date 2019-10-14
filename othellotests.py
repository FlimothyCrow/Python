import unittest
from othello import *


class OthelloTests(unittest.TestCase):
    def test_firstPlacement(self):
        emptyBoard = [[1, 2, 0],
                      [0, 0, 0]]

        self.assertEqual([[1, 1, 1],
                          [0, 0, 0]],
                         updateGame(emptyBoard, [0,2], 1))

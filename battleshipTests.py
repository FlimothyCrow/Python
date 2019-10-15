import unittest
from battleship import *


class battleshipTests(unittest.TestCase):
    def test_updateGame(self):
        emptyBoard = [[1, 0, 0],
                      [0, 0, 0]]

        self.assertEqual([[1, 0, 0],
                          [0, 0, 0]],
                         updateGame(emptyBoard, [0,0], 1))

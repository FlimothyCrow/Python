import unittest
from battleship import *


class battleshipTests(unittest.TestCase):
    def test_updateGame(self):
        emptyBoard = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]

        self.assertEqual([[0, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]],
                         updateGame(emptyBoard, [1,1], 1))

        self.assertEqual([[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 0, 0]],
                         updateGame(emptyBoard, [2, 2], 1))

        self.assertEqual([[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [1, 0, 0, 0]],
                         updateGame(emptyBoard, [3,0], 1))


    def test_hitMiss(self):
        emptyBoard = [[2, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]

        self.assertEqual(None, hitMiss(emptyBoard, [0, 0]))
        self.assertEqual(True, hitMiss(emptyBoard, [0, 1]))
# how to clone an object
#
    def test_moveValid(self):
        emptyBoard = [[1, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]
        self.assertEqual(False, moveValid(emptyBoard, [0,0]))

    # def test_playGame(self): WHAT'S THE BEST WAY TO TEST THIS?


    def test_gameOver(self):
        emptyBoard = [[1, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]
        self.assertEqual(True, gameOver(emptyBoard))


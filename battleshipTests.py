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

#other tests passed one by one but can't be tested in sequence without deep clone



    def test_hitMiss(self):
        emptyBoard = [[2, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]

        self.assertEqual(True, hitMiss(emptyBoard, [0, 0]))
        self.assertEqual(False, hitMiss(emptyBoard, [0, 1]))
# how to clone an object
#
    def test_moveValid(self):
        emptyBoard = [[1, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]
        self.assertEqual(True, moveValid(emptyBoard, [0,0]))

    # def test_playGame(self): WHAT'S THE BEST WAY TO TEST THIS?


    def test_gameContinue(self):
        emptyBoard = [[1, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]

        fullBoard = [[1, 0, 0, 0],
                      [9, 9, 9, 9],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]
        self.assertEqual(True, gameContinue(emptyBoard))
        self.assertEqual(None, gameContinue(fullBoard))

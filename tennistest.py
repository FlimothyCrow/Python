import unittest
from tennis import *


class tennistest(unittest.TestCase):
    """
    def test_score(self):
        self.assertEqual("love", score(0))
        self.assertEqual("fifteen", score(1))
        self.assertEqual("thirty", score(2))
        self.assertEqual("forty", score(3))

    """
    def test_whoWins(self):
        self.assertEqual("player 1", whoWins(1, 0))
        self.assertEqual("player 2", whoWins(1, 3))


    def test_returnLargest(self):
        listOfInputs = returnLargest([3, 1, -49, 39])
        self.assertEqual(39, listOfInputs)

    def test_removeDupes(self):
        listOfElements = removeDupes([1, "n", 39, "b", "b", 39, 238])
        self.assertEqual({39: 2, "b": 2}, listOfElements)

    def test_max(self):
        input1 = 2
        input2 = 2
        input3 = [1, 2, 5, 6]
        newUser = UserMainCode()
        maxResult = newUser.max(input1, input2, input3)
        self.assertEqual([[1, 2], [5,6]], maxResult)

    def test_max1(self):
        input1 = 3
        input2 = 3
        input3 = [1, 2, 5, 6, 238, 4]
        newUser = UserMainCode()
        maxResult = newUser.max(input1, input2, input3)
        self.assertEqual([[1, 2, 5], [6, 238, 4]], maxResult)


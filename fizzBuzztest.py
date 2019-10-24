import unittest
from fizzBuzz import *


class fizzBuzz(unittest.TestCase):

    jerks = [1, 2, 3, 4, 5, 6]


    def test_wordChanger(self):
    #    jerks = [1, 2, 3, 4, 5, 6]
        self.assertEqual([1, 2, 1, 4, 5, 1], wordChanger(self.jerks, 3, 1))
        self.assertEqual([1, 2, "jerks", 4, 5, "jerks"], wordChanger(self.jerks, 3, "jerks"))
        self.assertEqual([1, "schmo", "jerks", "schmo", 5, "jerks"], wordChanger([1, 2, "jerks", 4, 5, "jerks"], 2, "schmo"))

    def test_listRange(self):
        self.assertEqual([1, 2, 3, 4, 5], listRange(1, 6))


import unittest
from pazaak import *


class pazaakTest(unittest.TestCase):
    def test_playCard(self):
        self.assertEqual(1, playCard())

    #def test_chooseCard(self):
     #   self.assertEqual(1, chooseCard()) this passes without random.randint



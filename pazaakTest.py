import unittest
from pazaak import *


class pazaakTest(unittest.TestCase):
    def test_makeCard(self):
        card = makeCard()
        self.assertEqual("f", card.operator) # this passes without the randint generators
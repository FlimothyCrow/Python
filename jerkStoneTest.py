import unittest
from jerkStone import *


class jerkStoneTest(unittest.TestCase):

    def test_drawCard(self):
        newGameState = {'health': 30,
                     'mana': 10,
                     'hand': [1, 2, 3],
                     'deck': [4, 5, 7, 4, 3, 5, 8, 9, 9, 10, 10, 1, 2, 1]}

        tooManyCards = {'health': 30,
                     'mana': 10,
                     'hand': [1, 2, 3, 8, 9],
                     'deck': [0, 1, 2]}

        self.assertEqual({'health': 30,
                 'mana': 10,
                 'hand': [1, 2, 3, 4],
                 'deck': [5, 7, 4, 3, 5, 8, 9, 9, 10, 10, 1, 2, 1]}, drawCard(newGameState))

        self.assertEqual({'health': 30,
                'mana': 10,
                'hand': [1, 2, 3, 8, 9],
                'deck': [1, 2]}, drawCard(tooManyCards))

    def test_playCard(self):
        newGameState = {'health': 30,
                        'mana': 2,
                        'hand': [1, 2, 3],
                        'deck': [3, 5]}

        self.assertEqual({'health': 29,
                        'mana': 1,
                        'hand': [2, 3],
                        'deck': [3, 5]}, playCard(newGameState, 1))

    def test_dealDamage(self):
        state = {'health': 30,
                 'mana': 10,
                 'hand': [1, 2, 3],
                 'deck': [4, 5, 7]}
        self.assertEqual({'health': 25,
                          'mana': 10,
                          'hand': [1, 2, 3],
                          'deck': [4, 5, 7]}, dealDamage(state, 5))

    def test_validPlay(self):
        state1 = {'health': 30,
                 'mana': 2,
                 'hand': [8, 2, 3],
                 'deck': [4, 5, 7]}
        self.assertEqual(True, validPlay(state1, 2))
        self.assertEqual("mana", validPlay(state1, 4))
        self.assertEqual("card", validPlay(state1, 1))

    def test_restoreMana(self):
        manaState = {'health': 30,
                  'mana': 2,
                  'hand': [8, 2, 3],
                  'deck': [4, 5, 7]}

        self.assertEqual({'health': 30,
                  'mana': 3,
                  'hand': [8, 2, 3],
                  'deck': [4, 5, 7]}, restoreMana(manaState, 3))

    def test_endTurn(self):
        finishState = {'health': 30,
                  'mana': 2,
                  'hand': [8, 2, 3],
                  'deck': [4, 5, 7]}

        finishStateBleed = {'health': 30,
                       'mana': 2,
                       'hand': [8, 2, 3, 1],
                       'deck': [1]}

        self.assertEqual({'health': 30,
                  'mana': 4,
                  'hand': [8, 2, 3, 4],
                  'deck': [5, 7]}, endTurn(finishState, 4))

        self.assertEqual({'health': 29,
                          'mana': 4,
                          'hand': [8, 2, 3, 1, 1],
                          'deck': []}, endTurn(finishStateBleed, 4))
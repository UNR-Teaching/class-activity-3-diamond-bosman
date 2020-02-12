import unittest
from board import Board
from game import Game
from player import Player

class TestGameConstructor(unittest.TestCase):

    def test1(self):
        '''
        Test player X was instantiated properly.
        '''
        game = Game()
        player = Player('x', 1)
        self.assertAlmostEqual(game.playerx.val, player.val)

    def test2(self):
        '''
        Test player O was instantiated properly.
        '''
        game = Game()
        player = Player('o', -1)
        self.assertAlmostEqual(game.playero.val, player.val)

if __name__ == '__main__':
    unittest.main()
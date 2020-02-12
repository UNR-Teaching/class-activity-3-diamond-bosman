import unittest
from board import Board
from game import Game
from player import Player

class TestPlayerConstructor(unittest.TestCase):

    def test1(self):
        '''
        Test player constructor works with marker.
        '''
        player = Player('x', 1)
        self.assertEqual(player.marker, 'x')

    def test2(self):
        '''
        Test player constructor works with value.
        '''
        player = Player('x', 1)
        self.assertEqual(player.val, 1)

if __name__ == '__main__':
    unittest.main()

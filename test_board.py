import unittest
from board import Board
from game import Game
from player import Player

class TestMarkSquare(unittest.TestCase):

    def test1(self):
        '''
        Test on empty square.
        '''
        board = Board()
        board.mark_square(0, 2, 1)
        self.assertEqual(board.board[0][2], 1)

    def test2(self):
        '''
        Test on non-empty square.
        '''
        board = Board()
        board.mark_square(0, 2, 1)
        board.mark_square(0, 2, -1)
        self.assertEqual(board.board[0][2], 1)

class TestHasWinner(unittest.TestCase):

    def test1(self):
        '''
        Test on diagonal winner.
        '''
        board = Board()
        board.mark_square(0, 0, 1)
        board.mark_square(1, 1, 1)
        board.mark_square(2, 2, 1)
        self.assertEqual(board.has_winner(), "x")

    def test2(self):
        '''
        Test on other diagonal winner.
        '''
        board = Board()
        board.mark_square(2, 0, 1)
        board.mark_square(1, 1, 1)
        board.mark_square(0, 2, 1)
        self.assertEqual(board.has_winner(), "x")

    def test3(self):
        '''
        Test no winner with some squares marked.
        '''
        board = Board()
        board.mark_square(0, 2, 1)
        board.mark_square(1, 2, -1)
        board.mark_square(2, 2, 1)
        self.assertEqual(board.has_winner(), ".")

    def test4(self):
        '''
        Test no winner with no squares marked.
        '''
        board = Board()
        self.assertEqual(board.has_winner(), ".")

if __name__ == '__main__':
    unittest.main()

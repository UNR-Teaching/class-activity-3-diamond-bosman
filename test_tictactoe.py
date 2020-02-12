import unittest
from tictactoe import Board

class TestMethods(unittest.TestCase):

    def test_mark_square(self):
        board = Board()
        board.mark_square(2, 0, 'x')
        self.assertEqual(board.board[0][2], 'x')

    def test_row_last_complete(self):
        board = Board()
        board.mark_square(0, 2, 'x')
        board.mark_square(1, 2, 'x')
        board.mark_square(2, 2, 'x')
        board.has_winner
        self.assertEqual(board.has_winner(), "x")

    def test_row_first_complete(self):
        board = Board()
        board.mark_square(0, 0, 'o')
        board.mark_square(1, 0, 'o')
        board.mark_square(2, 0, 'o')
        board.has_winner
        self.assertEqual(board.has_winner, "o")


    def test_no_winner(self):
        board = Board()
        board.mark_square(0, 2, 'x')
        board.mark_square(1, 2, 'o')
        board.mark_square(2, 2, 'x')
        board.has_winner
        self.assertEqual(board.has_winner, "n")


if __name__ == '__main__':
    unittest.main()

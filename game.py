from player import Player
from board import Board

class Game:
    def __init__(self):
        self.playerx = Player('x', 1)
        self.playero = Player('o', -1)
        self.board = Board()
        self.finished = False
        self.player_x_start = True
    
    def get_moves(self, p):
        move = input("Give your move (row,column) player " + p.marker + ": ")
        move = move.split(',')
        for i, value in enumerate(move):
            temp_value = value.strip()
            move[i] = temp_value

        for value in move:
            if not value.isalnum():
                print("Value must be alphanumeric")
                return

        if len(move) != 2:
            print("Please give 2 values")
            return

        move[0] = int(move[0])
        move[1] = int(move[1])
        return move
    
    def check_full(self):
        if self.board.board_full():
            return True
        return False
    
    def switch_players(self):
        p = None
        if self.player_x_start:
            p = self.playerx
        else:
            p = self.playero
        self.player_x_start = not self.player_x_start
        return p

    def player_move(self, moves, p):
        self.board.mark_square(moves[0], moves[1], p.val)

    def check_winner(self):
        winner = self.board.has_winner()
        return winner
    
    def print_board(self):
        board = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                if self.board.board[i][j] == 1:
                    board[i][j] = 'x'
                elif self.board.board[i][j] == -1:
                    board[i][j] = 'o'
                else:
                    board[i][j] = '-'
        for row in board:
            print(row)

    def play_game(self):
        while not self.finished:
            if self.check_full():
                break
            self.print_board()
            p = self.switch_players()

            moves = self.get_moves(p)
            if moves is None:
                continue

            self.player_move(moves, p)
            winner = self.check_winner()

            if winner != '.':
                return 'Winner is ' + winner

        return 'Tie'


if __name__ == '__main__':
    game = Game()
    winner = game.play_game()
    print("{} has won!".format(winner))
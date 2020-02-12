from player import Player
from board import Board

class Game:
    def __init__(self):
        self.playerx = Player('x', 1)
        self.playero = Player('o', -1)
        self.board = Board()
        self.finished = False
        self.player_x_start = True

    def play_game(self):
        while not self.finished:
            if self.board.board_full():
                break

            if self.player_x_start:
                p = self.playerx
            else:
                p = self.playero

            move = input("Give your move (row,column) player " + p.marker + ": ")
            move = move.split(',')
            for i, value in enumerate(move):
                temp_value = value.strip()
                move[i] = temp_value

            for value in move:
                if not value.isalnum():
                    print("Value must be alphanumeric")
                    break

            if len(move) != 2:
                print("Please give 2 values")
                continue

            move[0] = int(move[0])
            move[1] = int(move[1])
            winner = self.board.mark_square(move[0], move[1], p.val)

            if winner != '.':
                return 'Winner is ' + winner

            self.player_x_start = not self.player_x_start
        return 'Tie'

if __name__ == '__main__':
    game = Game()
    winner = game.play_game()
    print("{} has won!".format(winner))
from board import Board
from game import Game
from player import Player

class TestIntegration:

	def check_finished(self):
        game = Game()
	    game.check_finished()

    def check_switch_player(self):
        game = Game()
        game.switch_player()

    def check_get_moves(self):
        game = Game()
        moves = game.get_moves

    def check_moves(self):
        '''
        This function checks that entered moves in the game class properly integrate with
        the board
        '''
        game = Game()
        moves = (0, 1)
        game.player_moves(moves, 1)
        

    

    

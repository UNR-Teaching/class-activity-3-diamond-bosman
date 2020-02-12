class Board(object):

    def __init__(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.size = 3
        self.winner = 'None'
    
    def mark_square(self, row, col, value):
        if self.board[row][col] != 0:
            return
        
        self.board[row][col] = value
        result = self.has_winner()

        return result
        

    def has_winner(self):
        # check rows
        rows = 0
        for i in range(self.size):
            rows = sum([self.board[i][0], self.board[i][1], self.board[i][2]])
            if abs(rows) == 3:
                break

        # check cols
        cols = 0
        for i in range(self.size):
            cols = sum([self.board[0][i], self.board[1][i], self.board[2][i]])
            if abs(cols) == 3:
                break

        # check diag
        diag = sum([self.board[0][0], self.board[1][1], self.board[2][2]])

        # check other diag
        other_diag = sum([self.board[2][0], self.board[1][1], self.board[0][2]])
    
        if 3 in (rows, cols, diag, other_diag):
            return 'x'
        if -3 in (rows, cols, diag, other_diag):
            return 'o'
        
        return '.'

    def board_full(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return False
        return True
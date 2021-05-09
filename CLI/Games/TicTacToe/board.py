import sys


class TicTacToe:
    def __init__(self):
        self.board = self.generate_board()  # INITIALIZES THE BOARD
        self.current_winner = None

    def __len__(self):
        return len(self.board)

    @staticmethod
    def score_board(player1, player2):
        return("\n\
               |{}|{}|\n\
               ----------\n\
               |{}|{}|".format(str(player1.piece).center(5), str(player2.piece).center(5), str(player1.score).center(5), str(player2.score).center(5)))
    
    @staticmethod
    def generate_board():
        SIZE = 3
        return [[' ' for i in range(SIZE)] for j in range(SIZE)]

    def __repr__(self):
        return("\n\
               -------------\n\
               |{}|{}|{}|\n\
               +---+---+---+\n\
               |{}|{}|{}|\n\
               +---+---+---+\n\
               |{}|{}|{}|\n\
               -------------\n".format(self.board[0][0].center(3), self.board[0][1].center(3), self.board[0][2].center(3),
                                       self.board[1][0].center(3), self.board[1][1].center(3), self.board[1][2].center(3),
                                       self.board[2][0].center(3), self.board[2][1].center(3), self.board[2][2].center(3))
                                       )
        
    def moves_left(self):
        empty_squares = []
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == ' ':
                    empty_squares.append((i, j))
        return empty_squares

    def num_moves_left(self):
        return len(self.moves_left())
    
    def make_move(self, row, column, player):
        empty_squares = self.moves_left()
        if (row, column) in empty_squares:
            self.board[row][column] = player
            if self.winner(player):
                self.current_winner = player
                return player
    
    def winner(self, player):
        """Returns True when a win condition has been satisfied."""
        # ROW WIN CONDITION
        def row_win():
            for i in range(len(self.board)):
                FLAG = True
                for j in range(len(self.board)):
                    if self.board[i][j] != player:
                        FLAG = False
                        continue
                if FLAG == True:
                    return FLAG
        
        def column_win():
            for i in range(len(self.board)):
                FLAG = True
                for j in range(len(self.board)):
                    if self.board[j][i] != player:
                        FLAG = False
                        continue
                if FLAG == True:
                    return FLAG

        def diagonal_win():
            """PROBLEM: NEED HELP WITH THE LEFT DIAGONAL WIN CONDITION"""
            for i in range(len(self.board)):
                FLAG = True
                for i in range(len(self.board)):
                    if self.board[i][i] != player:
                        FLAG = False
                        continue
                if FLAG == True:
                    return FLAG
            for i in range(len(self.board)):
                FLAG = True
                j = len(self.board) - i - 1
                if self.board[i][j] != player:
                    FLAG = False
                    return FLAG
            if FLAG == True:
                return FLAG

        if row_win() == True:
            return True
        elif column_win() == True:
            return True
        elif diagonal_win() == True:
            return True
        else:
            return False
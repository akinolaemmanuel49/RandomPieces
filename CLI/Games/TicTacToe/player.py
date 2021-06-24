from random import choice
from math import inf

class Player:
    def __init__(self, piece, score=0):
        self.piece = piece
        self.score = score

    def get_move(self):
        pass

class HumanPlayer(Player):
    def __init__(self, piece, score=0):
        super().__init__(piece, score)

    def get_move(self, game):
        row = int(input("row >"))
        column = int(input("col >"))
        if (row, column) not in game.moves_left():
            return self.get_move(game)
        else:
            return row, column

class RandomComputerPlayer(Player):
    def __init__(self, piece, score=0):
        super().__init__(piece, score)

    def get_move(self, game):
        row, column = choice(game.moves_left())
        return row, column

class SmartComputerPlayer(Player):
    def __init__(self, piece, score=0):
        super().__init__(piece, score)

    def get_move(self, game):
        if len(game.moves_left()) == 9:
            row, column = choice(game.moves_left())
            # row, column = 1, 1
        else:
            row, column = self.minimax(game, self.piece)['position']
        return row, column

    def minimax(self, state, player):
        max_player = self.piece     # itself
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            score = 0
            for i in range(len(state.board)):
                for j in range(len(state.board)):
                    if state.board[i][j] == ' ':
                        score += 1
            return {'position': None, 'score': score if other_player == max_player else (-1 * score)}
        elif state.moves_left() == []:
            score = 0
            return {'position': None, 'score': score}

        if player == max_player:
            best_move = {'position': None, 'score': -inf}
        else:
            best_move = {'position': None, 'score': inf}
        for possible_move in state.moves_left():
            state.make_move(possible_move[0], possible_move[1], player)
            simulation = self.minimax(state, other_player)

            # undo move
            state.board[possible_move[0]][possible_move[1]] = ' '
            state.current_winner = None
            simulation['position'] = possible_move

            if player == max_player:
                if simulation['score'] > best_move['score']:
                    best_move = simulation
            else:
                if simulation['score'] < best_move['score']:
                    best_move = simulation
        return best_move
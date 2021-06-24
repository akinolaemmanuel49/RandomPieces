import sys
from time import sleep
from board import TicTacToe
from player import Player, HumanPlayer, RandomComputerPlayer, SmartComputerPlayer

# DRIVER
def play(game, player1, player2):
    print(game)
    while True:
        for player in (player1, player2):
            if game.moves_left() == []:
                print(game)
                print("It's a tie!")
                game.board = game.generate_board()
                return play(game, player2, player1)
            move = player.get_move(game)
            if game.make_move(move[0], move[1], player.piece):
                print(game)
                if game.current_winner:
                    player.score += 1
                    print("{} WINS!!!".format(player.piece))
                    print(game.score_board(player1, player2))
                    game.current_winner = None
                    prompt = str(input("Do you want to try again (Y/N)")).strip()[0].upper()
                    if prompt == 'Y':
                        game.board = game.generate_board()
                        return play(game, player2, player1)
                    else:
                        print("\t\tFINAL SCORE")
                        print(game.score_board(player1, player2))
                        sys.exit("THANKS FOR PLAYING.")
            sleep(0.8)
            print(game)
            print("{} was placed at row: {}, col: {}".format(player.piece, 
                                                                    move[0], move[1])
                                                                    )

if __name__ == "__main__":
    game = TicTacToe()
    player1 = SmartComputerPlayer('X')
    player2 = SmartComputerPlayer('O')
    play(game, player1, player2)
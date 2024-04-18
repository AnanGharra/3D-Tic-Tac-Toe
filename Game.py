import random
from inputimeout import inputimeout, TimeoutOccurred
from Board import Board
from Player import Player

def game():
        board = Board()
        try:
            p1_name = str(input("Enter the first player's name (Plays as 'X'): "))
            p2_name = str(input("Enter the second player's name (Plays as 'O'): "))
            player1 = Player(p1_name, 'X')
            player2 = Player(p2_name, 'O')
            curr_player = random.choice([player1, player2])
        

            while not board.is_full():
                if not curr_player.play_move(board):
                    curr_player = player1 if curr_player == player2 else player2
                    continue
                if board.win_check(curr_player.symbol):
                    curr_player.wins += 1
                    print(f"Congratulations {curr_player.name}, You won!")
                    break
                curr_player = player1 if curr_player == player2 else player2
        
            if not board.win_check(player1.symbol) and not board.win_check(player2.symbol):
                print("Game over, it's a Draw!")

            print(f"Score: {player1.name} ({player1.wins}) - {player2.name} ({player2.wins})")
        
        except KeyboardInterrupt:
             print("\nClosing 3D-Tic-Tac-Toe... Bye!")
             exit()


if __name__ == '__main__':
     game()
    
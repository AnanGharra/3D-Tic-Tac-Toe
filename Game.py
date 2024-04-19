#!/usr/bin/env python3

import random
from Board import Board
from Player import Player
from colorama import Fore, Style

# Main game function to control the game flow.
def game():
        try:
            print(Fore.CYAN + Style.BRIGHT + "Welcome to 3D-Tic-Tac-Toe!")
            p1_name = str(input(Fore.GREEN + Style.BRIGHT + "Enter the first player's name (Plays as 'X'): "))
            p2_name = str(input(Fore.BLUE + Style.BRIGHT + "Enter the second player's name (Plays as 'O'): "))
            player1 = Player(p1_name, 'X')
            player2 = Player(p2_name, 'O')

            while True:
                board = Board() 
                curr_player = random.choice([player1, player2])
        
                while not board.is_full():
                    if not curr_player.play_move(board):
                        curr_player = player1 if curr_player == player2 else player2
                        continue
                    if board.win_check(curr_player.symbol):
                        curr_player.wins += 1
                        print(f"{Fore.LIGHTMAGENTA_EX}Congratulations {Fore.LIGHTMAGENTA_EX}{curr_player.name}, {Fore.LIGHTMAGENTA_EX}You won!")
                        break
                    curr_player = player1 if curr_player == player2 else player2

                if not board.win_check(player1.symbol) and not board.win_check(player2.symbol):
                    print(Fore.MAGENTA + "Game over, it's a Draw!")

                print(f"{Fore.MAGENTA}Score: {Fore.MAGENTA}{player1.name} ({Fore.MAGENTA}{player1.wins}) - {Fore.MAGENTA}{player2.name} ({Fore.MAGENTA}{player2.wins})")
                try:
                    another_game = input(Fore.CYAN + "Would you like to play another game? [yes/no]: ").lower()
                    if another_game == 'yes' or another_game == 'y':
                        board.reset()
                    elif another_game == 'no' or another_game == 'n':
                        print(Fore.RED + "\nClosing 3D-Tic-Tac-Toe... Bye!")
                        break
                except KeyboardInterrupt:
                    print(Fore.RED + "\nClosing 3D-Tic-Tac-Toe... Bye!")
                         
        
        except KeyboardInterrupt:
             print(Fore.RED + "\nClosing 3D-Tic-Tac-Toe... Bye!")
             exit()


if __name__ == '__main__':
     game()
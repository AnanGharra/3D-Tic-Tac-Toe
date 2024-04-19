#!/usr/bin/env python3

from Board import Board
from colorama import Fore, Style

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.wins = 0


    def play_move(self, board):
        if isinstance(board, Board):
            board.display()
            if self.symbol == "X":
                color = Fore.GREEN + Style.BRIGHT
            else:
                color = Fore.BLUE + Style.BRIGHT
            print(f"{color}{self.name}'s turn. You are '{color}{self.symbol}'.")
            cell_num = board.valid_move()
            if cell_num is None:
                return False
            if not board.play_move(cell_num, self.symbol):
                print(Fore.RED + "Cell is alredy taken. Please choose another cell to play.")
                return self.play_move(board)
            return True
        else:
            return False
import random
from inputimeout import inputimeout, TimeoutOccurred
from Board import Board


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.wins = 0


    def play_move(self, board):
        if isinstance(board, Board):
            board.display()
            print(f"{self.name}'s turn. You are '{self.symbol}'.")
            cell_num = board.valid_move()
            if cell_num is None:
                return False
            if not board.play_move(cell_num, self.symbol):
                print("Cell is alredy taken. Please choose another cell to play.")
                return self.play_move(board)
            return True
        else:
            return False
        
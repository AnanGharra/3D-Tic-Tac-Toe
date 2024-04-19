#!/usr/bin/env python3

from inputimeout import inputimeout, TimeoutOccurred
from colorama import Fore, Style, init

# Initialize colorama to reset.
init(autoreset=True)


# Board class definition to handle the 3D Tic-Tac-Toe board operations.
class Board:
    def __init__(self):
        #Initialize a list of 27 spaces representing a 3x3x3 Tic-Tac-Toe board
        self.cells = [" " for _ in range(27)]

    
    # Display the current state of the board with appropriate colors.
    def display(self):
        # Define colors for differen players.
        colors = {"X": Fore.GREEN + Style.BRIGHT, "O": Fore.BLUE + Style.BRIGHT, " ": Fore.WHITE}
        index = 0
        # Display the board layer by layer.
        for layer in range(3):
            print(Fore.YELLOW + f"Board {Fore.YELLOW}{layer+1}:")
            for row in range(3):
                print(" " * 10, end='')
                print("|", end='    ')
                for col in range(3):
                    if self.cells[index] != " ":
                        cell_val = self.cells[index]
                    else:
                        cell_val = index + 1
                    print(f"{colors[self.cells[index]]}{cell_val}    |", end='    ')
                    index += 1
                if row != 2:
                    print("\n" + " " * 10 + '-' * 34)
                else:
                    print()
            if layer != 2:
                print(" " * 10 + '-' * 34)
        print()


    # Check if the cells on the board are filled.
    def is_full(self):
        return all(cell != " " for cell in self.cells)
    

    # Place a move on the board if the chosen cell is empty.
    def play_move(self, cell_num, symbol):
        if self.cells[cell_num - 1] == " ":
            self.cells[cell_num - 1] = symbol
            return True
        else:
            return False
        

    # Check for winning compinations.
    def win_check(self, player):
         # Win possibilities that are predefined for simplicity. In total = 49
        wins = [
             # Horizontal lines in each layer:
             [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Layer 1
             [9, 10, 11], [12, 13, 14], [15, 16, 17],  # Layer 2
             [18, 19, 20], [21, 22, 23], [24, 25,26],  # Layer 3
             # Vertical lines in each layer:
             [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Layer 1
             [9, 12, 15], [10, 13, 16], [11, 14, 17],  # Layer 2
             [18, 21, 24], [19, 22, 25], [20, 23, 26],  # Layer 3
             # Diagonal lines in each layer:
             [0, 4, 8], [2, 4, 6],  # Layer 1
             [9, 13, 17], [11, 13, 15], # Layer 2
             [6, 15, 24], [7, 16, 25],  # Layer 3
             # Horizontal across layers:
             [0, 12, 24], [6, 12, 24], [1, 13, 25], [7, 13, 9], [2, 14, 26], [8, 14, 2],  # Columns Horizontal
             [0, 10, 20], [2, 10, 18], [3, 13, 23], [5, 13, 21], [6, 16, 26], [8, 16, 24],  # Rows Horizontal
             # Vertical across layers:
             [0, 9, 18], [1, 10, 19], [2, 11, 20],  # Row 1
             [3, 12, 21], [4, 13, 22], [5, 14, 23],  # Row 2
             [6, 15, 24], [7, 16, 25], [8, 17, 26],  # Row 3
             # Diagonal across layers:
             [0, 13, 26], [2, 13, 24], [6, 13, 20], [8, 13, 18]
        ]
        for possibile in wins:
            if all(self.cells[i] == player for i in possibile):
                return True
        return False
        
    
    # Get a valid move from the user, handling timeouts and  invalid inputs.
    def valid_move(self):
        while True:
            try:
                cell_num = int(inputimeout(prompt="Choose a cell number (1-27): ", timeout=60))
                if 1 <= cell_num <= 27:
                    return cell_num
                else:
                    print(Fore.RED + "Invalid cell number! Please choose a number between 1 and 27.")
            except TimeoutOccurred:
                print(Fore.LIGHTYELLOW_EX + "Too bad, Time's out! Switching players...")
                return None
            except ValueError:
                print(Fore.RED + "Invalid input! Please enter a number.")
            except KeyboardInterrupt:
                print(Fore.RED + "\nClosing 3D-Tic-Tac-Toe... Bye!")
                exit()
            
    
    # Reset the board for a new game.
    def reset(self):
        self.cells = [" " for _ in range(27)]
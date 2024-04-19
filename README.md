# 3D Tic-Tac-Toe

Welcome to the 3D Tic-Tac-Toe repository! This project brings the classic game of Tic-Tac-Toe into a three-dimensional playing field, increasing the complexity and fun. Built in Python, this game uses a console-based interface enhanced with colored outputs to provide an engaging user experience.

## Features

- **3D Gameplay:** Play Tic-Tac-Toe in a 3x3x3 grid, offering more challenging and strategic gameplay than the traditional 2D version.
- **Colorful Console Output:** Utilizes the Colorama library to make the gameplay more visually appealing.
- **Player Interactivity:** Support for two players with dynamic input and time-limited responses.
- **Error Handling:** Robust error handling to manage incorrect inputs and ensure a smooth gameplay experience.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What you need to install the software:

- Python 3.6 or higher
- Colorama
- inputimeout

You can install the required packages using pip:

```bash
pip install colorama inputimeout
```

### Installing

1. Clone the repository:

```bash
git clone https://github.com/AnanGharra/3D-Tic-Tac-Toe
```

2. Navigate to the directory:

```bash
cd 3D-Tic-Tac-Toe
```

3. Ensure the files are executable:

```bash
chmod +x Baord.py Player.py Game.py
```

4. Run the script:

```bash
./Game.py
```


## How to play

- The game is played on a 3x3x3 grid, visualized in three separate layers.
- Players take turns choosing a cell in the grid by entering a number between 1 and 27.
- The objective is to align three of your marks (X or O) horizontally, vertically, or diagonally.
- For each play there is a time of 60 seconds, then the play switches to the other player.
- The game ends when all cells are filled or a player wins.


## Acknowledgments

- Colorama Library: For making rhe Python console colorful and easier to read.
- Inputimeout Library: For adding input timeout in Python.


**Enjoy playing 3D Tic-Tac-Toe! :smile: :v:

# Sudoku Solver

## Overview
This project consists of two main components: a Sudoku solving algorithm (`solver.py`) and a graphical user interface to interact with the solver (`solverGUI.py`). The solver uses a backtracking algorithm to find the solution to the Sudoku puzzle, and the GUI is built using Pygame to provide an interactive experience.

## Features
- **Solve Sudoku puzzles**: Automatically solve puzzles using the backtracking algorithm.
- **Interactive GUI**: Manually input Sudoku puzzles and visualize the solving process.
- **Real-time puzzle validation**: Check the validity of the current state of the puzzle as you fill in the cells.

## Installation

To get started with this project, you need to have Python installed on your machine along with Pygame for the graphical interface.

1. Clone the repository:

    ```git clone https://github.com/acharyasamir/sudoku-solver.git```

2. Navigate to the project directory:

    ```cd sudoku-solver```

3. Install the required dependencies:

    ```pip install pygame```


## Usage

To run the Sudoku solver with the GUI, execute the following command in the terminal:

    ```python solverGUI.py```


Use the mouse to click on a cell and select a number to fill the cell. Press the space bar to initiate the solving process and visualize the algorithm in action.

## License

[MIT License](LICENSE)
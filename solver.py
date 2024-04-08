def solve(bo):
    """
    Solves a sudoku board using backtracking
    :param bo: 2d list of ints representing the board
    :return: bool, True if a solution is found, False otherwise
    """
    find = find_empty(bo)
    if not find:
        return True  # Solution found
    row, col = find

    for num in range(1, 10):
        if valid(bo, num, (row, col)):
            bo[row][col] = num
            if solve(bo):
                return True
            bo[row][col] = 0  # Reset on backtrack

    return False  # Trigger backtracking


def valid(bo, num, pos):
    """
    Checks if a number can be placed at the specified position
    :param bo: 2d list of ints representing the board
    :param num: int, the number to place
    :param pos: tuple, (row, col) position to check
    :return: bool, True if the move is valid, False otherwise
    """
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def find_empty(bo):
    """
    Finds the first empty space in the board
    :param bo: 2d list of ints representing the board
    :return: tuple, (row, col) of the first empty position, or None if full
    """
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # Row, col
    return None


def print_board(bo):
    """
    Prints the board in a human-readable format
    :param bo: 2d List of ints representing the board
    :return: None
    """
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")
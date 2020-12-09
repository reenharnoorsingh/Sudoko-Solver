# Sodoku Solver in Python
# solve sudoku using backtracking!


def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> represented with -1
    for r in range(9):
        for c in range(9):  # range(9) is 0, 1, 2, ... 8
            if puzzle[r][c] == -1:
                return r, c

    return None, None  # if no spaces in the puzzle are empty


def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True or False
    row_vals = puzzle[row]
    if guess in row_vals:
        return False  # if we've repeated, then our guess is not valid!

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row // 3) * 3  # 10 // 3 = 3, 5 // 3 = 1, 1 // 3 = 0
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True


def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)
    if row is None:  # this is true if our find_next_empty function returns None, None
        return True

    for guess in range(1, 10):  # range(1, 10) is 1, 2, 3, ... 9
        # check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # if this is a valid guess, then place it at that spot on the puzzle
            puzzle[row][col] = guess
            # recursively call our solver!
            if solve_sudoku(puzzle):
                return True

        # it not valid or if nothing gets returned true, then we need to backtrack and try a new number
        puzzle[row][col] = -1

    return False


if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)

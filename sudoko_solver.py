# Sudoku Solver in Python
# using backtracking!


def find_empty_block(puzzle): #finds the next row, col on the puzzle that is not filled
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row, col

    return None, None #if no space in the puzzle is empty

def is_valid(puzzle,guess, row, col):
    

def sudoku_solver(puzzle):
    row, col = find_empty_block(puzzle)

    if row is None:
        return True
    
    for guess in range(1,10):
        if is_valid(puzzle, guess, row, col):
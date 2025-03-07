# Based on https://www.youtube.com/watch?v=G_UYXzGuqvM


# [9, 0, 0, 0, 0, 3, 0, 0, 0]
# [0, 0, 3, 0, 0, 0, 4, 0, 8]
# [0, 0, 6, 0, 9, 0, 2, 0, 0]
# [0, 1, 0, 0, 0, 4, 0, 0, 2]
# [5, 0, 0, 0, 6, 0, 0, 0, 1]
# [0, 0, 9, 0, 0, 0, 6, 0, 0]
# [0, 0, 8, 1, 0, 0, 0, 7, 0]
# [2, 0, 0, 0, 0, 0, 1, 6, 4]
# [0, 9, 0, 0, 5, 0, 0, 0, 0]
# 25


import numpy as np
import random

M_SIZE = 9
GRID_SIZE = 3

settings = {
    "CLASSIC": 1,
    "KNIGHT": 0,
    "NON_CONSEC": 0,
    "KING": 0,
    "SANDWICH": 0,

}

# A = np.array([
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ])






def is_valid(A, i, j, value, settings):
    if settings["CLASSIC"]:
        #check row + column
        for rc in range(M_SIZE):
            if A[i][rc] == value or A[rc][j] == value:
                return False
        # check square
        for r in range((i//GRID_SIZE) * GRID_SIZE, (i//GRID_SIZE) * GRID_SIZE + GRID_SIZE):
            for c in range((j//GRID_SIZE) * GRID_SIZE, (j//GRID_SIZE) * GRID_SIZE + GRID_SIZE):
                if A[r][c] == value:
                    return False

    if settings["KNIGHT"]:
        # Define knight moves (relative positions)
        knight_moves = [
            (-2, -1), (-2, 1), (2, -1), (2, 1),
            (-1, -2), (-1, 2), (1, -2), (1, 2)
        ]
        for di, dj in knight_moves:
            ni, nj = i + di, j + dj
            if 0 <= ni < M_SIZE and 0 <= nj < M_SIZE and A[ni][nj] == value:
                return False  # Found the same value in a knight move position

    if settings["NON_CONSEC"]:
        # nonconsecutive
        if (
                (i + 1 < M_SIZE and A[i + 1][j] == value + 1) or
                (j + 1 < M_SIZE and A[i][j + 1] == value + 1) or
                (i - 1 >= 0 and A[i - 1][j] == value + 1) or
                (j - 1 >= 0 and A[i][j - 1] == value + 1) or

                (value > 1 and (
                (i + 1 < M_SIZE and A[i + 1][j] == value - 1) or
                (j + 1 < M_SIZE and A[i][j + 1] == value - 1) or
                (i - 1 >= 0 and A[i - 1][j] == value - 1) or
                (j - 1 >= 0 and A[i][j - 1] == value - 1)))
        ):
            return False

    return True


def solve(A):
    # go to all empty
    for i in range(M_SIZE):
        for j in range(M_SIZE):
            if A[i][j] == 0:
                # try x if x is is_valid
                for x in range(1, M_SIZE + 1):
                    if is_valid(A, i, j, x, settings=settings):
                        A[i][j] = x
                        if solve(A):
                            return True, A
                        A[i][j] = 0
                return False
    return True, A


def unique_solve(A):
    def count_solutions(A):
        # Helper function to count valid solutions
        solution_count = 0

        # Go through all empty spaces
        for i in range(M_SIZE):
            for j in range(M_SIZE):
                if A[i][j] == 0:
                    # Try numbers from 1 to M_SIZE
                    for x in range(1, M_SIZE + 1):
                        if is_valid(A, i, j, x, settings=settings):
                            A[i][j] = x
                            solution_count += count_solutions(A)
                            A[i][j] = 0  # Reset for backtracking

                            # If more than 1 solution found, return early
                            if solution_count > 1:
                                return solution_count

                    return solution_count  # No solution found for this path
        return 1  # Found one valid solution

    # Count unique solutions
    unique_solution_count = count_solutions(A)

    # If there's exactly one unique solution, return True
    if unique_solution_count == 1:
        return True, A
    else:
        return False


def generate_full_board():
    board = [[0] * 9 for _ in range(9)]
    def fill_board():
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    nums = [i for i in range(1, 10)]
                    random.shuffle(nums)
                    for num in nums:
                        if is_valid(board, row, col, num, settings=settings):
                            board[row][col] = num
                            if fill_board():
                                return True
                            board[row][col] = 0
                    return False
        return True
    fill_board()
    return board


def remove_numbers(board, attempts):
    puzzle = [row[:] for row in board]
    while attempts > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        while puzzle[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        backup = puzzle[row][col]
        puzzle[row][col] = 0
        board_copy = [r[:] for r in puzzle]
        if not unique_solve(board_copy):
            puzzle[row][col] = backup  # Restore if removing breaks uniqueness
        attempts -= 1
    return puzzle

def generate_sudoku(difficulty):
    full_board = generate_full_board()
    # print(full_board)
    return remove_numbers(full_board, M_SIZE*M_SIZE - difficulty)








def find_min(dif, NUM = 100):
    minp = 0
    minc = 81
    list = []
    for i in range(NUM):
        print(f"{i}/{NUM}")
        sudoku_puzzle = generate_sudoku(difficulty=dif)
        non_zero_count = sum(1 for row in sudoku_puzzle for num in row if num != 0)
        list.append(non_zero_count)
        if non_zero_count < minc:
            minp = sudoku_puzzle
            minc = non_zero_count

    for row in minp:
        print(row)
    print(minc)

    return minp


import json

def replace_zeros_with_null(grid):
    modified_grid =  [[None if num == 0 else num for num in row] for row in grid]
    for row in modified_grid:
        print(json.dumps(row), end=",\n")

# find_min(2)



# Example grid
grid = [
    [0, 0, 0, 0, 7, 4, 0, 0, 3],
    [9, 0, 0, 0, 0, 0, 8, 0, 0],
    [6, 4, 0, 0, 2, 0, 5, 0, 9],
    [4, 0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 0, 5, 0, 0, 0, 7],
    [0, 2, 0, 3, 0, 0, 0, 0, 0],
    [0, 0, 8, 7, 6, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 5],
    [0, 5, 7, 0, 0, 0, 2, 0, 0] 
]

# Replace 0s with None
new_grid = replace_zeros_with_null(grid)

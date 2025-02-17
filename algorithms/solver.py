# Based on https://www.youtube.com/watch?v=G_UYXzGuqvM
import numpy as np
import random

M_SIZE = 9
GRID_SIZE = 3

settings = {
    "CLASSIC": 1,
    "KNIGHT": 1,
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

A = np.array([
    [0, 0, 0, 3, 2, 0, 1, 7, 5],
    [1, 0, 0, 9, 7, 5, 4, 0, 0],
    [7, 5, 2, 4, 1, 6, 3, 9, 8],
    [0, 0, 5, 8, 0, 0, 0, 0, 7],
    [0, 1, 0, 0, 0, 0, 2, 4, 0],
    [0, 0, 4, 6, 3, 0, 0, 5, 9],
    [0, 0, 7, 0, 0, 3, 0, 0, 1],
    [0, 3, 0, 0, 8, 4, 0, 6, 0],
    [8, 2, 6, 0, 0, 0, 0, 0, 4]
])




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


def generate_full_board():
    board = [[0] * 9 for _ in range(9)]
    def fill_board():
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    nums = list(range(1, 10))
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


def remove_numbers(board, difficulty=40):
    puzzle = [row[:] for row in board]
    attempts = difficulty
    while attempts > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        while puzzle[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        backup = puzzle[row][col]
        puzzle[row][col] = 0
        board_copy = [r[:] for r in puzzle]
        if not solve(board_copy):
            puzzle[row][col] = backup  # Restore if removing breaks uniqueness
        attempts -= 1
    return puzzle

def generate_sudoku(difficulty=40):
    full_board = generate_full_board()
    # print(full_board)
    return remove_numbers(full_board, difficulty)

# # Example usage:
# sudoku_puzzle = generate_sudoku()
# for row in sudoku_puzzle:
#     print(row)

_, solution = solve(A)
print(solution)
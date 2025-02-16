# Based on https://www.youtube.com/watch?v=G_UYXzGuqvM
import numpy as np


M_SIZE = 9
GRID_SIZE = 3

settings = {
    "CLASSIC": 1,
    "KNIGHT": 1,
    "NON_CONSEC": 0,
    "KING": True,
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
    [7, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [9, 5, 0, 0, 0, 0, 0, 4, 3],
    [3, 0, 0, 0, 0, 0, 0, 9, 8],
    [0, 0, 1, 0, 0, 0, 2, 0, 0],
    [5, 0, 0, 7, 0, 8, 0, 0, 4]
])




def possible(A, i, j, value, settings):
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
            if A[i, j] == 0:

                # try x if x is possible
                for x in range(1, M_SIZE + 1):
                    if possible(A, i, j, x, settings=settings):
                        A[i, j] = x
                        solve(A)
                        A[i, j] = 0
                return
    print(A)


solve(A)
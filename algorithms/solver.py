# Based on https://www.youtube.com/watch?v=G_UYXzGuqvM
import numpy as np


M_SIZE = 9
GRID_SIZE = 3

A = np.array([
    [0, 9, 0, 0, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 6, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 7, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 2, 0],
    [0, 0, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 8, 0]
])




def possible(A, i, j, value):
    #check row + column
    for rc in range(M_SIZE):
        if A[i][rc] == value or A[rc][j] == value:
            return False
    # check square
    for r in range((i//GRID_SIZE) * GRID_SIZE, (i//GRID_SIZE) * GRID_SIZE + GRID_SIZE):
        for c in range((j//GRID_SIZE) * GRID_SIZE, (j//GRID_SIZE) * GRID_SIZE + GRID_SIZE):
            if A[r][c] == value:
                return False

    # knight

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
                    if possible(A, i, j, x):
                        A[i, j] = x
                        solve(A)
                        A[i, j] = 0
                return
    print(A)


solve(A)
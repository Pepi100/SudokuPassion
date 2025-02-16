# Implemented algorithms

## 1. Sudoku Solver

This file contains a simple backtracking implementation for solving any sudoku puzzle, by trying any possible combinations.



### How it works

This algorithm is heavily inspired by Computerphile's [Python Sudoku Solver](https://www.youtube.com/watch?v=G_UYXzGuqvM) video. It consists of two main functions. The first (_**solve**_) is a recursive function used to solve the puzzle by trying every possible digit for any possible slot. The second function (_**possible**_) is the _brains of the operation_ 🧠. This function is used to check whether the last placed number brakes any of currently set board rules. 

#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens on an
N×N chessboard. Write a program that solves the N queens problem.
    * Usage: nqueens N
    - If the user called the program with the wrong number of arguments, print
    Usage: nqueens N, followed by a new line, and exit with the status 1
    * where N must be an integer greater or equal to 4
    - If N is not an integer, print N must be a number, followed by a new line,
    and exit with the status 1
    - If N is smaller than 4, print N must be at least 4, followed by a new
    line, and exit with the status 1
    * The program should print every possible solution to the problem
    - One solution per line
    - Format: see example
    - You don’t have to print the solutions in a specific order
    * You are only allowed to import the sys module
"""
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except BaseException:
        print('N must be a number')
        sys.exit(1)
    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    column_set = set()
    pos_set = set()
    neg_set = set()
    chessboard = [[0 for _ in range(n)] for _ in range(n)]

    def solve_n_queens(row):
        if row == n:
            board_copy = [row[:] for row in chessboard]
            print_n_queens(board_copy)
            return

        for col in range(n):
            if col in column_set or (row + col) in pos_set or (row - col) in neg_set:  # noqa
                continue
            column_set.add(col)
            pos_set.add(row + col)
            neg_set.add(row - col)
            chessboard[row][col] = 1

            solve_n_queens(row + 1)

            column_set.remove(col)
            pos_set.remove(row + col)
            neg_set.remove(row - col)
            chessboard[row][col] = 0

    def print_n_queens(result):
        queens_positions = []
        for i in range(n):
            for j in range(n):
                if result[i][j] == 1:
                    queens_positions.append([i, j])
        print(queens_positions)
        queens_positions.clear()

    solve_n_queens(0)

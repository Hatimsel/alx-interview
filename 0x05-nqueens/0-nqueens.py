#!/usr/bin/python3
"""N queens"""
import sys


def print_usage_and_exit():
    """Print usage message and exit"""
    print("Usage: nqueens N")
    exit(1)


def print_error_and_exit(message):
    """Print error message and exit"""
    print(message)
    exit(1)


if len(sys.argv) != 2:
    print_usage_and_exit()

if not sys.argv[1].isdigit():
    print_error_and_exit("N must be a number")

N = int(sys.argv[1])

if N < 4:
    print_error_and_exit("N must be at least 4")


def queens(n, row=0, columns=[], diagonals1=[], diagonals2=[]):
    """Generate all valid board positions for N queens"""
    if row == n:
        yield columns
    else:
        for col in range(n):
            if (col not in columns and
                    row - col not in diagonals1 and
                    row + col not in diagonals2):
                yield from queens(n, row + 1,
                                  columns + [col],
                                  diagonals1 + [row - col],
                                  diagonals2 + [row + col])


def solve(n):
    """Solve the N queens problem and print all solutions"""
    for solution in queens(n):
        print([[i, solution[i]] for i in range(n)])


if __name__ == '__main__':
    solve(N)

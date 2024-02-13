#!/usr/bin/python3

"""This module solves the Nqueens puzzle and prints
    the solution in the form [[r, c], [r, c], [r, c], [r, c]
    where r and c stand for row and column"""


import sys


def Nqueens(n):

    """"Solves the Nqueen puzzle"""
    sol = []
    board = [[0 * n for i in range(n)] for i in range(n)]
    if Q_Help(board, 0) is True:
        return


def Q_Help(board, col):
    """Puts the queen in a square"""
    if col >= len(board):
        return True
    for i in range(len(board)):
        if Is_Safe(board, i, col):
            board[i][col] = 1
            if Q_Help(board, col+1) is True:
                return True
            board[i][col] = 0
            return False


def Is_Safe(board, row, col):
    """Checks if it is a safe square """
    for i in range(col):
        if board[row][i] == 1:
            return False

    i = row
    j = col
    while i >= 0 and j > 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row
    j = col
    while j >= 0 and i < len(board):
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    elif sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    elif int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    Nqueens(4)

#!/usr/bin/python3
"""This module contains a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elemnts of a matrix"""
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(msg)
    if not all(isinstance(sublist, list) for sublist in matrix):
        raise TypeError(msg)
    if not all(isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError(msg)
    len_m = len(matrix[0])
    if not all(len(row) == len_m for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    newmatrix = [[round((i / div), 2) for i in row] for row in matrix]

    return(newmatrix)

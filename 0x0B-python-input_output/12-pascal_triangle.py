#!/usr/bin/python3
"""This contains pascal_triangle function"""


def pascal_triangle(n):

    """
    returns a list of lists of integers
    representing the Pascal's triangle of n
    """

    triangle = [[] for i in range(0, n)]
    if n <= 0:
        return triangle

    for i in range(0, n):
        triangle[i].append(1)
        for j in range(1, i):
            tmp = triangle[i - 1][j] + triangle[i - 1][j-1]
            triangle[i].append(tmp)
        if i > 0:
            triangle[i].append(1)
    return triangle

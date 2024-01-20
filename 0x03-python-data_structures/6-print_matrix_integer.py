#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for i in matrix:
        len_i = len(i)
        for j in range(len_i):
            if j == len_i - 1:
                print("{:d}".format(i[j]), end="")
            else:
                print("{:d}".format(i[j]), end=" ")
        print()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
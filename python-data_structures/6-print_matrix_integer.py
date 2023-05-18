#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    m = len(matrix)
    x = '\n'.join([''.join(['{:d}'.format(item) for item in row]) for row in matrix])
    return x

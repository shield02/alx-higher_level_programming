#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        mx = list(map(lambda x: x**2, matrix[i]))
        new_matrix.append(mx)
    return new_matrix

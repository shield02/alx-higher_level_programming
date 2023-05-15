#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for left in range(len(matrix)):
        for right in range(len(matrix[left])):
            print("{:d}".format(matrix[left][right]), end="")
            if (right != len(matrix[left]) - 1):
                print(" ", end="")
        print("")

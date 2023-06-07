#!/usr/bin/python3
"""
    The module - matrix_divided
    Defines a function for matrix division.
"""


def matrix_divided(matrix, div):
    """Divide each element of the matrix.
    Args:
        matrix: List of lists of type ints or floats.
        div: The divisor of type int or float.
    Raises:
        TypeError: Matrix contains non-numbers.
        TypeError: Matrix contains rows of not equal sizes.
        TypeError: Div is not an int or float.
        ZeroDivisionError: Div is 0.
    Returns:
        A new matrix of the division operation.
    """
    if (not isinstance(matrix, list) 
            or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(item, int) or isinstance(item, float))
                    for item in [el for row in matrix for el in row])):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    try:
        return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
    except ZeroDivisionError:
        raise ZeroDivisionError("division by zero")

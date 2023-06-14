#!/usr/bin/python3
"""Pascal triangle module"""


def pascal_triangle(n):
    """Creates a list of list of integers
    Args:
        n (int): size of the triangle
    Raises:
        Nothing
    Returns:
        pascal (list): empty or list of list of integers
    """
    if n <= 0:
        return []
    pascal = []
    row = []
    for x in range(n):
        next_row = []
        for y in range(x + 1):
            if x == 0 or y == 0 or x == y:
                next_row.append(1)
            else:
                next_row.append(row[y] + row[y - 1])
        row = next_row
        pascal.append(next_row)
    return pascal

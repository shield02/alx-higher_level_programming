#!/usr/bin/python3
"""Multiply two matrix the hard way"""


def matrix_mul(m_a, m_b):
    """This function multiplies two matrices
    Args:
        m_a: (list of list) First matrix
        m_b: (list of list) Second matrix
    Raises:
        TypeError: If either m_a or m_b is not a list.
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        ValueError: If either m_a or m_b is empty.
        TypeError: If m_a and m_b element is not a int or float.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied
    Returns:
        A matrix (list of list)
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise isinstance("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(elem, int) or isinstance(elem, float)
            for elem in [elem for row in m_a for elem in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(elem, int) or isinstance(elem, float)
            for elem in [elem for row in m_b for elem in row]):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_b_i = []
    for r in range(len(m_b[0])):
        nr = []
        for c in range(len(m_b)):
            nr.append(m_b[c][r])
        m_b_i.append(nr)

    res_mat = []
    for row in m_a:
        nr = []
        for col in m_b_i:
            mul_r = 0
            for i in range(len(m_b_i[0])):
                mul_r += row[i] * col[i]
            nr.append(mul_r)
        res_mat.append(nr)

    return res_mat
    
#!/usr/bin/python3
"""
Module name: lazy_matrix_mul
Matrix multiplication with NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplication of two matrices.
    Args:
        m_a: first matrix.
        m_b: second matrix.
    Raises:
        Nothing
    Returns:
        Matrix
    """

    return (np.matmul(m_a, m_b))

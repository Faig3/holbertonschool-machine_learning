#!/usr/bin/env python3
"""
Module to calculate the inverse of a matrix.
"""


def inverse(matrix):
    """
        Calculates the inverse of a matrix.

        Args:
            matrix (list of lists): matrix to invert.

        Returns:
            list of lists of floats: inverse of matrix,
            or None if matrix is singular.

        Raises:
            TypeError: If matrix is not a list of lists.
            ValueError: If matrix is not a non-empty square matrix.
        """
    if not isinstance(matrix, list) or not all(isinstance(matrix, list) for row in matrix):
        raise TypeError("Matrix must be a list of lists")
        return None
    if len(matrix[0]) != len(matrix) or matrix == []:
        raise ValueError("matrix must be a non-empty square matrix")
    inverse_matrix = np.linalg.inv(matrix)
    if np.linalg.det(matrix) != 0:
        return inverse_matrix
    else:
        return None

#!/usr/bin/env python3
"""
Module to calculate the inverse of a matrix.
"""


def inverse(matrix):
    """
    Calculate the inverse of a matrix.

    Args:
        matrix (list of lists): Matrix to invert.

    Returns:
        list of lists: The inverse of the matrix.
        None: If the matrix is singular.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not a non-empty square matrix.
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    det = _det(matrix)

    if det == 0:
        return None

    if n == 1:
        return [[1 / det]]

    adj = _adj(matrix)

    return [[adj[i][j] / det for j in range(n)] for i in range(n)]


def _det(matrix):
    """
    Calculate the determinant of a matrix.

    Args:
        matrix (list of lists): Matrix to calculate determinant for.

    Returns:
        int or float: Determinant of the matrix.
    """
    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return (
            matrix[0][0] * matrix[1][1]
            - matrix[0][1] * matrix[1][0]
        )

    det = 0

    for j in range(n):
        sub = [
            [matrix[i][k] for k in range(n) if k != j]
            for i in range(1, n)
        ]
        det += ((-1) ** j) * matrix[0][j] * _det(sub)

    return det


def _submatrix(matrix, i, j):
    """
    Create a submatrix by removing one row and one column.

    Args:
        matrix (list of lists): Original matrix.
        i (int): Row index to remove.
        j (int): Column index to remove.

    Returns:
        list of lists: Submatrix without row i and column j.
    """
    n = len(matrix)

    return [
        [matrix[r][c] for c in range(n) if c != j]
        for r in range(n) if r != i
    ]


def minor(matrix):
    """
    Calculate the minor matrix of a matrix.

    Args:
        matrix (list of lists): Matrix to calculate minors for.

    Returns:
        list of lists: Minor matrix.
    """
    n = len(matrix)

    if n == 1:
        return [[1]]

    result = []

    for i in range(n):
        row = []

        for j in range(n):
            sub = _submatrix(matrix, i, j)
            row.append(_det(sub))

        result.append(row)

    return result


def cofactor(matrix):
    """
    Calculate the cofactor matrix of a matrix.

    Args:
        matrix (list of lists): Matrix to calculate cofactors for.

    Returns:
        list of lists: Cofactor matrix.
    """
    n = len(matrix)

    if n == 1:
        return [[1]]

    result = []

    for i in range(n):
        row = []

        for j in range(n):
            sub = _submatrix(matrix, i, j)
            sign = (-1) ** (i + j)
            row.append(sign * _det(sub))

        result.append(row)

    return result


def _adj(matrix):
    """
    Calculate the adjugate matrix of a matrix.

    Args:
        matrix (list of lists): Matrix to calculate adjugate for.

    Returns:
        list of lists: Adjugate matrix.
    """
    n = len(matrix)

    if n == 1:
        return [[1]]

    cof = cofactor(matrix)

    return [[cof[j][i] for j in range(n)] for i in range(n)]

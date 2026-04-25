#!/usr/bin/env python3
"""Defines the function matrix_transpose(matrix)"""


def matrix_transpose(matrix):
    """Function that returns the transpose of a 2D matrix"""
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

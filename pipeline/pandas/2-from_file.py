#!/usr/bin/env python3
"""Module that loads data from a file as a pd.DataFrame."""
import pandas as pd


def from_file(filename, delimiter):
    """Load data from a file as a pd.DataFrame.

    Args:
        filename (str): The file to load from.
        delimiter (str): The column separator.

    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    return pd.read_csv(filename, delimiter=delimiter)

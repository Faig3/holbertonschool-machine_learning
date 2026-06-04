#!/usr/bin/env python3
"""Module that creates a DataFrame from a numpy ndarray."""
import pandas as pd


def from_numpy(array):
    """Create a pd.DataFrame from a np.ndarray.

    Args:
        array (np.ndarray): The array to convert to a DataFrame.

    Returns:
        pd.DataFrame: DataFrame with columns labeled in alphabetical order.
    """
    cols = [chr(65 + i) for i in range(array.shape[1])]
    return pd.DataFrame(array, columns=cols)

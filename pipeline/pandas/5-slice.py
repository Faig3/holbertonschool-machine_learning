#!/usr/bin/env python3
"""Module that slices a pd.DataFrame."""
import pandas as pd


def slice(df):
    """Extract specific columns and select every 60th row.

    Args:
        df (pd.DataFrame): DataFrame to slice.

    Returns:
        pd.DataFrame: Sliced DataFrame with High, Low, Close, Volume_BTC.
    """
    # Extract specific columns
    df = df[['High', 'Low', 'Close', 'Volume_BTC']]

    # Select every 60th row
    df = df[::60]

    return df

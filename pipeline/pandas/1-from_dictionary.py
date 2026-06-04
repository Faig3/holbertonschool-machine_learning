#!/usr/bin/env python3
"""Module that creates a pd.DataFrame from a dictionary.

This script creates a DataFrame with two columns (First, Second)
and four rows labeled A, B, C, and D.
"""
import pandas as pd

# Create a DataFrame from a dictionary with labeled rows
df = pd.DataFrame(
    {
        'First': [0.0, 0.5, 1.0, 1.5],    # float values
        'Second': ['one', 'two', 'three', 'four']  # string values
    },
    index=['A', 'B', 'C', 'D']  # row labels
)

print(df)

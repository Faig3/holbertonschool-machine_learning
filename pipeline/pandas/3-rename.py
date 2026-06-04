#!/usr/bin/env python3
import pandas as pd

def rename(df):
    """Rename Timestamp column and convert to datetime, display Datetime and Close.

    Args:
        df (pd.DataFrame): DataFrame containing a Timestamp column.

    Returns:
        pd.DataFrame: Modified DataFrame with Datetime and Close columns only.
    """
    # Rename Timestamp column to Datetime
    df =df.rename(columns={'Timestamp': 'Datetime'})

    # Convert timestamp values to datetime values
    df['Datetime'] = pd.to_datetime(df['Datetime'], unit='s')

    # Display only Datetime and Close columns
    df = df[['Datetime', 'Close']]

    return df

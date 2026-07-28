import pandas as pd
from pandas import DataFrame


def transform_data_draft(df: DataFrame):
    # Remove any duplicate rows in each DataFrame
    df = df.drop_duplicates()

    # Replace missing values in numeric columns with the mean
    df = df.fillna(df.mean())

    # Replace missing values in categorical columns with the mode
    df = df.fillna((df.mode().iloc[0]))

    # Convert data types: Convert columns into their appropriate data types for further processing using the astype()
    # function.
    # Convert column to appropriate data types
    df['CRASH_DATE'] = pd.to_datetime(df['CRASH_DATE'], format = '%m/%d/%Y')
    df['POSTED_SPEED_LIMIT'] = df['POSTED_SPEED_LIMIT'].astype('int32')

    return df



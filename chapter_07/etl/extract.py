# import dependent modules
from os import PathLike

import pandas as pd

# extract data
def extract_data(filepath: str | PathLike[str]) -> pd.DataFrame:
    """
       Simple Extract Function in Python with Error Handling
       :param filepath: str, file path to CSV data
       :output: pandas dataframe, extracted from CSV data
    """
    try:
        # Read the CSV file and store it in a dataframe
        df = pd.read_csv(filepath)
        return df

    # Handle exception if any of the files are missing
    except FileNotFoundError as e:
        print(f"Error: {filepath}")
        return pd.DataFrame()
    # Handle any other exceptions
    except Exception as e:
        print(f"Error reading file: {e}")
        return pd.DataFrame

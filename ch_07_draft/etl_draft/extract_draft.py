import pandas as pd
from pathlib import Path

try:
    # Read the traffic crashes CSV file and store it in a dataframe
    print(Path.cwd())
    df_crashes = pd.read_csv("data/traffic_crashes.csv")
    # Read the traffic crash vehicles CSV file and store it in a dataframe
    df_vehicles = pd.read_csv("data/traffic_crash_vehicle.csv")

    # Read the traffic crash People CSV and store it in a dataframe
    df_people = pd.read_csv("chapter_07/data/traffic_crash_people.csv")

except FileNotFoundError as e:
    # Handle exception if any of the files are missing
    print(f"Error: {e}")

except Exception as e:
    # Handle any other exceptions
    print(f"Error: {e}")



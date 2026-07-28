import pandas as pd


def extract_data():

    try:
        # Read the traffic crashes CSV file and store it in a DataFrame
        df_crashes = pd.read_csv(
            "data/traffic_crashes.csv"
        )

        # Read the traffic crash vehicles CSV file and store it in a DataFrame
        df_vehicles = pd.read_csv(
            "data/traffic_crash_vehicle.csv"
        )

        # Read the traffic crash people CSV file and store it in a DataFrame
        df_people = pd.read_csv(
            "data/traffic_crash_people.csv"
        )

        # Return extracted DataFrames for further transformation
        return (
            df_crashes,
            df_vehicles,
            df_people
        )

    except FileNotFoundError as e:
        # Handle exception if any of the input files are missing
        raise FileNotFoundError(
            f"File not found: {e}"
        )

    except Exception as e:
        # Handle any other exceptions during the extraction process
        raise Exception(
            f"Extraction error: {e}"
        )

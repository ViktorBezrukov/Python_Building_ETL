# TODO Import packages required...


def run_pipeline():

    # Extract
    crashes_df, vehicles_df, people_df = extract_data()

    # Transform
    crashes_df = transform_crashes(crashes_df)
    vehicles_df = transform_vehicles(vehicles_df)
    people_df = transform_people(people_df)

    # Load
    load_crashes(crashes_df)
    load_vehicles(vehicles_df)
    load_people(people_df)


if __name__ == "__main__":
    run_pipeline()

import extract_draft
from ch_07_draft.transform_draft import transform_data_draft


def run_pipeline():

    # Extract
    crashes_df, vehicles_df, people_df = extract_draft.extract_data()

    # Transform
    crashes_df = transform_data_draft(crashes_df)
    vehicles_df = transform_data_draft(vehicles_df)
    people_df = transform_data_draft(people_df)

    # Load
    load_crashes(crashes_df)
    load_vehicles(vehicles_df)
    load_people(people_df)


if __name__ == "__main__":
    run_pipeline()

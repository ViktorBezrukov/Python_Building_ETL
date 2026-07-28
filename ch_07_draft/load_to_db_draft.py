import psycopg


def load_vehicle(df, db_config):
    insert_query = """
    INSERT INTO chicago_dmv.vehicle (
        crash_unit_id,
        crash_id,
        crash_date,
        vehicle_id,
        vehicle_make,
        vehicle_model,
        vehicle_year,
        vehicle_type
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """

    with psycopg.connect(**db_config) as conn:
        with conn.cursor() as cur:
            cur.executemany(
                insert_query,
                df.itertuples(index=False, name=None)
            )

        conn.commit()

    conn.commit()

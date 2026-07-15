import pandas as pd

# Left DataFrame
df_crashes = pd.DataFrame({
    "crash_record_id": [101, 102, 103, 104],
    "weather": ["Clear", "Rain", "Snow", "Fog"]
})

# Right DataFrame
df_vehicles = pd.DataFrame({
    "crash_record_id": [101, 101, 103, 105],
    "vehicle_type": ["Car", "Truck", "Motorcycle", "Bus"]
})

print(df_crashes)
print()
print(df_vehicles)

merged_df = df_crashes.merge(df_vehicles, how = 'inner', on='crash_record_id')
print(merged_df)
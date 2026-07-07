import pandas as pd

df = pd.read_csv('../data/h9gi-nx95.csv')
print(df.head())

df_parquet = pd.read_parquet("../data/yellow_tripdata_2022-01.parquet")
print(df_parquet.head())

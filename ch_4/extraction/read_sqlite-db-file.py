import sqlite3
import pandas as pd
conn = sqlite3.connect("../data/movies.sqlite")
cursor = conn.cursor()

cursor.execute("SELECT * FROM sqlite_master ;")
tables = cursor.fetchall()
print(tables)

conn_pd = sqlite3.connect("../data/movies.sqlite")

df = pd.read_sql_query("SELECT * FROM movies LIMIT 10;", conn_pd)

print(df)
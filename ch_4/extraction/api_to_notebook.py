import json
import certifi
import pandas as pd
import requests

url = "https://data.cityofnewyork.us/resource/h9gi-nx95.json?$limit=500"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    print(df.head())
else:
    print("Error", response.status_code)
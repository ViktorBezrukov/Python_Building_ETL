import pandas as pd

df_crashes = pd.read_csv("data/traffic_crashes.csv")
#result = df_crashes.head()
#print(result)
df_crashes.info()
print("="*30)
res = df_crashes.isnull().sum()
print(res)




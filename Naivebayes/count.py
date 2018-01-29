import pandas as pd

Location=r'C:\Users\kiran\Desktop\data tuning\trycsv\exptrain.csv'

df=pd.read_csv(Location)

print("df count:")
print(df.count().values[0])
print("df RS count")
print(df[df['Class']=='RS'].count().values[0])
print("df NRS count")
print(df[df['Class']=='NRS'].count().values[0])

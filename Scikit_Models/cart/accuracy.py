import pandas as pd
import numpy as np

Location =r'C:\Users\kiran\Desktop\cart\op.csv'
df = pd.read_csv(Location)

Location2 =r'C:\Users\kiran\Desktop\cart\desireop.csv'
df2 = pd.read_csv(Location2)

count=0;
for index,row in df.iterrows():
    if(row['Class']==df2.loc[index,'Class']):
        count=count+1

accuracy=count/df.count().values[0]*100
print(accuracy)

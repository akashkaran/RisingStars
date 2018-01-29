import pandas as pd

from pandas import DataFrame,read_csv

Location = r'C:\Users\kiran\Desktop\data tuning\trycsv\TestDataSet.csv'

df = pd.read_csv(Location)
df['Class']= 'NA'
hs_median = 64.0
rpi_median = 17.08
avg_median = 21.05
sr_median = 72.93
fpi_median = 0.058823529
bpbf_median = 0.07317073
max_inns =df['Inns'].max()
min_inns = df['Inns'].min()

#labelling players as RS or NRS using algorithm
for index,row in df.iterrows():
    if(row['SR']>=sr_median):
        if((row['Avrg']<avg_median)and(row['R/I']<rpi_median)):
            df.loc[index,'Class']='NRS'
        else:
            count=0;
            if(row['HS']>=hs_median):
                count += 1
            if(row['50/I']>=fpi_median):
                count += 1
            if(row['6+4/BF']>=bpbf_median):
                count += 1

            if(count>1):
                df.loc[index,'Class']='RS'
            else:
                df.loc[index,'Class']='NRS'

    else:
        df.loc[index,'Class']='NRS'


print(" count:")
print(df.count().values[0])
print(" RS count")
print(df[df['Class']=='RS'].count().values[0])
print(" NRS count")
print(df[df['Class']=='NRS'].count().values[0])

#finaldf.sort_values(['id'],ascending=[True], inplace=True)
df.to_csv('desireop.csv',mode = 'w')

import pandas as pd

from pandas import DataFrame,read_csv

Location = r'C:\Users\kiran\Desktop\data tuning\trycsv\TestDataSet.csv'

df = pd.read_csv(Location)
#df['Class']= 'NA'
hs_median = df['HS'].median()
rpi_median = df['R/I'].median()
avg_median = df['Avrg'].median()
sr_median = df['SR'].median()
hpi_median = df['100/I'].median()
fpi_median = df['50/I'].median()
bpbf_median = df['6+4/BF'].median()
max_inns =df['Inns'].max()
min_inns = df['Inns'].min()
print("hs median = %s"%(hs_median))
print("RPI median = %s"%(rpi_median))
print("AVG median = %s"%(avg_median))
print("SR median = %s"%(sr_median))
print("HPI median = %s"%(hpi_median))
print("FPI median = %s"%(fpi_median))
print("BPBF median = %s"%(bpbf_median))
print(max_inns)
print(min_inns)


#labelling players as RS or NRS using algorithm
for index,row in df.iterrows():
    if((row['SR']>=sr_median)and(row['Avrg']>=avg_median)and(row['R/I']>=rpi_median)and(row['HS']>=hs_median)and(row['100/I']>=hpi_median)and(row['50/I']>=fpi_median)and(row['6+4/BF']>=bpbf_median)):
        df.loc[index,'Class']='RS'

    else:
        df.loc[index,'Class']='NRS'

print("df count:")
print(df.count().values[0])
print("df RS count")
print(df[df['Class']=='RS'].count().values[0])
print("df NRS count")
print(df[df['Class']=='NRS'].count().values[0])

#finaldf.sort_values(['id'],ascending=[True], inplace=True)
df.to_csv('expectedresult.csv',mode = 'w')

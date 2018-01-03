import pandas as pd

from pandas import DataFrame,read_csv

Location = r'C:\Users\kiran\Desktop\mlpractice\rawdata.csv'

df = pd.read_csv(Location)
df['Class']= 'NA'
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

# labelling data set For 10 to 50 innings

# calculating median for each features
df1 = df[(df['Inns']>=10)&(df['Inns']<=50)]
hs_median1 = df1['HS'].median()
rpi_median1 = df1['R/I'].median()
avg_median1 = df1['Avrg'].median()
sr_median1 = df1['SR'].median()
hpi_median1 = df1['100/I'].median()
fpi_median1 = df1['50/I'].median()
bpbf_median1 = df1['6+4/BF'].median()
max_inns =df1['Inns'].max()
min_inns = df1['Inns'].min()
print("HS median = %s"%(hs_median1))
print("RPI median = %s"%(rpi_median1))
print("AVG median = %s"%(avg_median1))
print("SR median = %s"%(sr_median1))
print("HPI median = %s"%(hpi_median1))
print("FPI median = %s"%(fpi_median1))
print("BPBF median = %s"%(bpbf_median1))
print(max_inns)
print(min_inns)

#labelling players as RS or NRS using algorithm
for index,row in df1.iterrows():
    if(row['SR']>=sr_median1):
        if((row['Avrg']<avg_median1)and(row['R/I']<rpi_median1)):
            df1.loc[index,'Class']='NRS'
        else:
            count=0;
            if(row['HS']>=hs_median1):
                count += 1
            if(row['100/I']>=hpi_median1):
                count=count+1
            if(row['50/I']>=fpi_median1):
                count += 1
            if(row['6+4/BF']>=bpbf_median1):
                count += 1

            if(count>2):
                df1.loc[index,'Class']='RS'
            else:
                df1.loc[index,'Class']='NRS'

    else:
        df1.loc[index,'Class']='NRS'

print(df1.count().values[0])
print(df1[df1['Class']=='RS'].count().values[0])
print(df1[df1['Class']=='NRS'].count().values[0])

# labelling data set For 51 to 99 innings

# calculating median for each features
df2 = df[(df['Inns']>=51)&(df['Inns']<=99)]
hs_median2 = df2['HS'].median()
rpi_median2 = df2['R/I'].median()
avg_median2 = df2['Avrg'].median()
sr_median2 = df2['SR'].median()
hpi_median2 = df2['100/I'].median()
fpi_median2 = df2['50/I'].median()
bpbf_median2 = df2['6+4/BF'].median()
max_inns =df2['Inns'].max()
min_inns = df2['Inns'].min()
print("HS median2 = %s"%(hs_median2))
print("RPI median2 = %s"%(rpi_median2))
print("AVG median2 = %s"%(avg_median2))
print("SR median2 = %s"%(sr_median2))
print("HPI median2 = %s"%(hpi_median2))
print("FPI median2 = %s"%(fpi_median2))
print("BPBF median2 = %s"%(bpbf_median2))
print(max_inns)
print(min_inns)

#labelling players as RS or NRS using algorithm
for index,row in df2.iterrows():
    if(row['SR']>=sr_median2):
        if((row['Avrg']<avg_median2)and(row['R/I']<rpi_median2)):
            df2.loc[index,'Class']='NRS'
        else:
            count=0;
            if(row['HS']>=hs_median2):
                count=count+1
            if(row['100/I']>=hpi_median2):
                count=count+1
            if(row['50/I']>=fpi_median2):
                count=count+1
            if(row['6+4/BF']>=bpbf_median2):
                count=count+1

            if(count>2):
                df2.loc[index,'Class']='RS'
            else:
                df2.loc[index,'Class']='NRS'

    else:
        df2.loc[index,'Class']='NRS'

print("Df2 total count %d"%(df2.count().values[0]))
print("Df2 rs count%d"%(df2[df2['Class']=='RS'].count().values[0]))
print("Df2 nrs cpunt%d"%(df2[df2['Class']=='NRS'].count().values[0]))


frames = [df1,df2]
finaldf = pd.concat(frames)
print("Finaldf count:")
print(finaldf.count().values[0])
print("Finaldf RS count")
print(finaldf[finaldf['Class']=='RS'].count().values[0])
print("Finaldf NRS count")
print(finaldf[finaldf['Class']=='NRS'].count().values[0])

finaldf.sort_values(['id'],ascending=[True], inplace=True)
finaldf.to_csv('finaltraindataset.csv',mode = 'w')

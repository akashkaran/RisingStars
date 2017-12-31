import pandas as pd

from pandas import DataFrame,read_csv

Location = r'C:\Users\kiran\Downloads\Span.csv'

df = pd.read_csv(Location)
df['Class']= 'NA'
nopi_median = df['NO/I'].median()
rpi_median = df['R/I'].median()
avg_median = df['Avrg'].median()
sr_median = df['SR'].median()
hpi_median = df['100/I'].median()
fpi_median = df['50/I'].median()
bpbf_median = df['6+4/BF'].median()
max_inns =df['Inns'].max()
min_inns = df['Inns'].min()
print("NOPI median = %s"%(nopi_median))
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
nopi_median1 = df1['NO/I'].median()
rpi_median1 = df1['R/I'].median()
avg_median1 = df1['Avrg'].median()
sr_median1 = df1['SR'].median()
hpi_median1 = df1['100/I'].median()
fpi_median1 = df1['50/I'].median()
bpbf_median1 = df1['6+4/BF'].median()
max_inns =df1['Inns'].max()
min_inns = df1['Inns'].min()
print("NOPI median = %s"%(nopi_median1))
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
    if(row['NO/I']>=nopi_median1):
        if((row['Avrg']<avg_median1)and(row['SR'])<sr_median1):
            df1.loc[index,'Class']='NRS'
        else:
            count=0;
            if(row['NO/I']>=nopi_median1):
                count=count+1
            if(row['50/I']>=fpi_median1):
                count=count+1
            if(row['6+4/BF']>=bpbf_median1):
                count=count+1

            if(count>=2):
                df1.loc[index,'Class']='RS'
            else:
                df1.loc[index,'Class']='NRS'

    else:
        df1.loc[index,'Class']='NRS'

print(df1.count())
print(df1[df1['Class']=='RS'].count())
print(df1[df1['Class']=='NRS'].count())

# labelling data set For 51 to 99 innings

# calculating median for each features
df2 = df[(df['Inns']>=51)&(df['Inns']<=99)]
nopi_median2 = df2['NO/I'].median()
rpi_median2 = df2['R/I'].median()
avg_median2 = df2['Avrg'].median()
sr_median2 = df2['SR'].median()
hpi_median2 = df2['100/I'].median()
fpi_median2 = df2['50/I'].median()
bpbf_median2 = df2['6+4/BF'].median()
max_inns =df2['Inns'].max()
min_inns = df2['Inns'].min()
print("NOPI median = %s"%(nopi_median2))
print("RPI median = %s"%(rpi_median2))
print("AVG median = %s"%(avg_median2))
print("SR median = %s"%(sr_median2))
print("HPI median = %s"%(hpi_median2))
print("FPI median = %s"%(fpi_median2))
print("BPBF median = %s"%(bpbf_median2))
print(max_inns)
print(min_inns)

#labelling players as RS or NRS using algorithm
for index,row in df2.iterrows():
    if(row['NO/I']>=nopi_median2):
        if((row['Avrg']<avg_median2)and(row['SR'])<sr_median2):
            df2.loc[index,'Class']='NRS'
        else:
            count=0;
            if(row['NO/I']>=nopi_median2):
                count=count+1
            if(row['50/I']>=fpi_median2):
                count=count+1
            if(row['6+4/BF']>=bpbf_median2):
                count=count+1

            if(count>=2):
                df2.loc[index,'Class']='RS'
            else:
                df2.loc[index,'Class']='NRS'

    else:
        df2.loc[index,'Class']='NRS'

print(df2.count())
print(df2[df2['Class']=='RS'].count())
print(df2[df2['Class']=='NRS'].count())


frames = [df1,df2]
finaldf = pd.concat(frames)
print(finaldf.count())
print(finaldf[finaldf['Class']=='RS'].count())
finaldf.sort_values(['R/I'],ascending=[False], inplace=True)
#finaldf.to_csv('traindataset.csv',index='false',header='false')

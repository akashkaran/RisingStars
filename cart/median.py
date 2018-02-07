import pandas as pd

from pandas import DataFrame,read_csv

Location = r'C:\Users\kiran\Desktop\RisingStars\cart\exptrain.csv'

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




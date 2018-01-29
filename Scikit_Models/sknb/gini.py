import pandas as pd

Location=r'C:\Users\kiran\Desktop\data tuning\trycsv\exptrain.csv'

df=pd.read_csv(Location)

hs_median = 64.0
rpi_median = 17.08
avg_median = 21.05
sr_median = 72.93
fpi_median = 0.058823529
bpbf_median = 0.07317073

total=df.count().values[0]

gt_rpi_df = df[df['R/I']>=rpi_median]
lt_rpi_df = df[df['R/I']<rpi_median]

total_gt_rpi = gt_rpi_df.count().values[0]
total_lt_rpi = lt_rpi_df.count().values[0]

gt_rpi_rs = gt_rpi_df[gt_rpi_df['Class']=='RS'].count().values[0]
lt_rpi_rs = lt_rpi_df[lt_rpi_df['Class']=='RS'].count().values[0]

gt_rpi_nrs=total_gt_rpi - gt_rpi_rs
lt_rpi_nrs=total_lt_rpi - lt_rpi_rs

gini_gt_rpi=(gt_rpi_rs/total_gt_rpi)**2+(gt_rpi_nrs/total_gt_rpi)**2

gini_lt_rpi=(lt_rpi_rs/total_lt_rpi)**2+(lt_rpi_nrs/total_lt_rpi)**2

gini_rpi=gini_gt_rpi*(total_gt_rpi/total)+gini_lt_rpi*(total_lt_rpi/total)

print(gini_rpi)


gt_hs_df = df[df['HS']>=hs_median]
lt_hs_df = df[df['HS']<hs_median]

total_gt_hs = gt_hs_df.count().values[0]
total_lt_hs = lt_hs_df.count().values[0]

gt_hs_rs = gt_hs_df[gt_hs_df['Class']=='RS'].count().values[0]
lt_hs_rs = lt_hs_df[lt_hs_df['Class']=='RS'].count().values[0]

gt_hs_nrs=total_gt_hs - gt_hs_rs
lt_hs_nrs=total_lt_hs - lt_hs_rs

gini_gt_hs=(gt_hs_rs/total_gt_hs)**2+(gt_hs_nrs/total_gt_hs)**2

gini_lt_hs=(lt_hs_rs/total_lt_hs)**2+(lt_hs_nrs/total_lt_hs)**2

gini_hs=gini_gt_hs*(total_gt_hs/total)+gini_lt_hs*(total_lt_hs/total)

print(gini_hs)

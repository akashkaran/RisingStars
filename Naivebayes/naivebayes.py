import pandas as pd
import numpy as np

Location =r'C:\Users\kiran\Desktop\RisingStars\Naivebayes\exptrain.csv'
df = pd.read_csv(Location)
df['PRS'] = 0
#1) calculating prior probability

#1.1) Total number of Rising star players
total_RS = df['Class'][df['Class']=='RS'].count()
#1.2) Total number of Not rising star players
total_NRS = df['Class'][df['Class']=='NRS'].count()
#1.3) Total players
total_players = df['Class'].count()

#1.4)calculating probability of RS
P_RS = total_RS/total_players
#1.5) calculating probability of NRS
P_NRS = total_NRS/total_players


#2) Calculating likelihood probability

#2.1) Group data by class and calculate means of each feature
data_means=df.groupby('Class').mean()
#2.2) Group the data by class and calculate variance of each feature
data_variance=df.groupby('Class').var()

#2.3) Mean of each feature belongs to class RS
RS_hs_mean = data_means['HS'][data_means.index == 'RS'].values[0]
RS_rpi_mean = data_means['R/I'][data_means.index == 'RS'].values[0] 
RS_avg_mean = data_means['Avrg'][data_means.index == 'RS'].values[0]
RS_sr_mean = data_means['SR'][data_means.index == 'RS'].values[0]
RS_fpi_mean = data_means['50/I'][data_means.index == 'RS'].values[0]
RS_bpbf_mean = data_means['6+4/BF'][data_means.index == 'RS'].values[0]

#2.4) variance of each feature belongs to class RS
RS_hs_var = data_variance['HS'][data_variance.index == 'RS'].values[0]
RS_rpi_var = data_variance['R/I'][data_variance.index == 'RS'].values[0] 
RS_avg_var = data_variance['Avrg'][data_variance.index == 'RS'].values[0]
RS_sr_var = data_variance['SR'][data_variance.index == 'RS'].values[0]
RS_fpi_var = data_variance['50/I'][data_variance.index == 'RS'].values[0]
RS_bpbf_var = data_variance['6+4/BF'][data_variance.index == 'RS'].values[0]

#2.5) Mean of each feature belongs to class RS
NRS_hs_mean = data_means['HS'][data_means.index == 'NRS'].values[0]
NRS_rpi_mean = data_means['R/I'][data_means.index == 'NRS'].values[0] 
NRS_avg_mean = data_means['Avrg'][data_means.index == 'NRS'].values[0]
NRS_sr_mean = data_means['SR'][data_means.index == 'NRS'].values[0]
NRS_fpi_mean = data_means['50/I'][data_means.index == 'NRS'].values[0]
NRS_bpbf_mean = data_means['6+4/BF'][data_means.index == 'NRS'].values[0]

#2.6) variance of each feature belongs to class RS
NRS_hs_var = data_variance['HS'][data_variance.index == 'NRS'].values[0]
NRS_rpi_var = data_variance['R/I'][data_variance.index == 'NRS'].values[0] 
NRS_avg_var = data_variance['Avrg'][data_variance.index == 'NRS'].values[0]
NRS_sr_var = data_variance['SR'][data_variance.index == 'NRS'].values[0]
NRS_fpi_var = data_variance['50/I'][data_variance.index == 'NRS'].values[0]
NRS_bpbf_var = data_variance['6+4/BF'][data_variance.index == 'NRS'].values[0]

#2.7) Function to calculate likelihood Probability
def feature_given_class(feature,class_mean,class_var):
   p=1/(np.sqrt(2*np.pi*class_var))*np.exp((-(feature-class_mean)**2)/(2*class_var))
   return p

#3)Naive bayes function(calculatng posterior probability for each class)
def nb(hs,rpi,avg,sr,fpi,hpi,bpbf,df,index):
    posterior_RS = P_RS*feature_given_class(hs,RS_hs_mean,RS_hs_var)*\
                   feature_given_class(rpi,RS_rpi_mean,RS_rpi_var)*\
                   feature_given_class(avg,RS_avg_mean,RS_avg_var)*\
                   feature_given_class(sr,RS_sr_mean,RS_sr_var)*\
                   feature_given_class(fpi,RS_fpi_mean,RS_fpi_var)*\
                   feature_given_class(bpbf,RS_bpbf_mean,RS_bpbf_var)
    
    posterior_NRS = P_NRS*feature_given_class(hs,NRS_hs_mean,NRS_hs_var)*\
                   feature_given_class(rpi,NRS_rpi_mean,NRS_rpi_var)*\
                   feature_given_class(avg,NRS_avg_mean,NRS_avg_var)*\
                   feature_given_class(sr,NRS_sr_mean,NRS_sr_var)*\
                   feature_given_class(fpi,NRS_fpi_mean,NRS_fpi_var)*\
                   feature_given_class(bpbf,NRS_bpbf_mean,NRS_bpbf_var)

    df.loc[index,'rating']=((posterior_RS-posterior_NRS)/posterior_RS)*1000

    if(posterior_RS>posterior_NRS):
       
       df.loc[index,'PRS']=posterior_RS
       return 'RS'
    else:
       df.loc[index,'PRS']=posterior_RS
       return 'NRS'

#testing for testdata csv

Location =r'C:\Users\kiran\Desktop\data tuning\trycsv\TestDataSet.csv'
df3 = pd.read_csv(Location)
df3['Class']='NA'
df3['rating']='0'
df3 = df3[(df3['Inns']>=10)]

for index,row in df3.iterrows():
   df3.loc[index,'Class']=nb(row['HS'],row['R/I'],row['Avrg'],row['SR'],row['50/I'],row['100/I'],row['6+4/BF'],df3,index)

print(df3.count().values[0])
print(df3[df3['Class']=='RS'].count().values[0])
print(df3[df3['Class']=='NRS'].count().values[0])
#df3.sort_values(['PRS'],ascending=[False], inplace=True)
df3.to_csv('output.csv',index='false',header='false')
print(df['Class'])








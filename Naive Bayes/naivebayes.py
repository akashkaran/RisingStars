import pandas as pd
import numpy as np

Location =r'C:\Users\kiran\Desktop\mlpractice\traindataset.csv'
df = pd.read_csv(Location)

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
RS_nopi_mean = data_means['NO/I'][data_means.index == 'RS'].values[0]
RS_rpi_mean = data_means['R/I'][data_means.index == 'RS'].values[0] 
RS_avg_mean = data_means['Avrg'][data_means.index == 'RS'].values[0]
RS_sr_mean = data_means['SR'][data_means.index == 'RS'].values[0]
RS_fpi_mean = data_means['50/I'][data_means.index == 'RS'].values[0]
RS_bpbf_mean = data_means['6+4/BF'][data_means.index == 'RS'].values[0]

#2.4) variance of each feature belongs to class RS
RS_nopi_var = data_variance['NO/I'][data_variance.index == 'RS'].values[0]
RS_rpi_var = data_variance['R/I'][data_variance.index == 'RS'].values[0] 
RS_avg_var = data_variance['Avrg'][data_variance.index == 'RS'].values[0]
RS_sr_var = data_variance['SR'][data_variance.index == 'RS'].values[0]
RS_fpi_var = data_variance['50/I'][data_variance.index == 'RS'].values[0]
RS_bpbf_var = data_variance['6+4/BF'][data_variance.index == 'RS'].values[0]

#2.5) Mean of each feature belongs to class RS
NRS_nopi_mean = data_means['NO/I'][data_means.index == 'NRS'].values[0]
NRS_rpi_mean = data_means['R/I'][data_means.index == 'NRS'].values[0] 
NRS_avg_mean = data_means['Avrg'][data_means.index == 'NRS'].values[0]
NRS_sr_mean = data_means['SR'][data_means.index == 'NRS'].values[0]
NRS_fpi_mean = data_means['50/I'][data_means.index == 'NRS'].values[0]
NRS_bpbf_mean = data_means['6+4/BF'][data_means.index == 'NRS'].values[0]

#2.6) variance of each feature belongs to class RS
NRS_nopi_var = data_variance['NO/I'][data_variance.index == 'NRS'].values[0]
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
def nb(nopi,rpi,avg,sr,fpi,bpbf):
    posterior_RS = P_RS*feature_given_class(nopi,RS_nopi_mean,RS_nopi_var)*\
                   feature_given_class(rpi,RS_rpi_mean,RS_rpi_var)*\
                   feature_given_class(avg,RS_avg_mean,RS_avg_var)*\
                   feature_given_class(sr,RS_sr_mean,RS_sr_var)*\
                   feature_given_class(fpi,RS_fpi_mean,RS_fpi_var)*\
                   feature_given_class(bpbf,RS_bpbf_mean,RS_bpbf_var)
    
    posterior_NRS = P_NRS*feature_given_class(nopi,NRS_nopi_mean,NRS_nopi_var)*\
                   feature_given_class(rpi,NRS_rpi_mean,NRS_rpi_var)*\
                   feature_given_class(avg,NRS_avg_mean,NRS_avg_var)*\
                   feature_given_class(sr,NRS_sr_mean,NRS_sr_var)*\
                   feature_given_class(fpi,NRS_fpi_mean,NRS_fpi_var)*\
                   feature_given_class(bpbf,NRS_bpbf_mean,NRS_bpbf_var)

    if(posterior_RS>posterior_NRS):
        print("Player is Rising Star")
    else:
        print("Player is Not Rising Star")

#testing for new players
#Q de Cock
print("Q de Cock:")
nb(0.052631578,50.31578947,53.11,94.84,0.368421052,0.113095238)
#N Dickwella
print("N Dickwella:")
nb(0.038461538,31.76923077,33.04,96.04,0.153846153,0.11744186)
#Hardik Pandya
print("Hardik Pandya")
nb(0.157894736,29.31578947,34.81,120.56,0.210526315,0.1406924)
#Shreyas Iyer
print("Shreyas Iyer")
nb(0,54,54,101.25,0.666666,0.13125)









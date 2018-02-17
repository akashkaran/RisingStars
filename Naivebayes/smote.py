import pandas as pd
from collections import Counter
from imblearn.over_sampling import SMOTE
Location = r'C:\Users\kiran\Desktop\batsman\nb\temptrainset.csv'
df=pd.read_csv(Location)
df=df[['HS','Avg','SR','50/I','6+4/BF','Class']]
x = df[['HS','Avg','SR','50/I','6+4/BF']]
y = df['Class']

print('Original dataset shape {}'.format(Counter(y)))
sm = SMOTE(random_state=42)
sx,sy=sm.fit_sample(x,y)
print('Resampled dataset shape {}'.format(Counter(sy)))

sdf = pd.DataFrame(sx)
sdf.columns= ['HS','Avg','SR','50/I','6+4/BF']
sdf['Class']=sy
sdf.to_csv('TrainDataSet.csv',mode = 'w')

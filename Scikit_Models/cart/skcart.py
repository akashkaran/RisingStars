import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
Location=r'C:\Users\kiran\Desktop\cart\exptrain.csv'

df=pd.read_csv(Location)



model = DecisionTreeClassifier()
model.fit(df[['R/I','HS','Avrg','SR','50/I','6+4/BF']],df['Class'])
print(model)

Location =r'C:\Users\kiran\Desktop\cart\TestDataSet.csv'
df3 = pd.read_csv(Location)
df3['Class']='NA'
df3['rating']='0'
df3 = df3[(df3['Inns']>=10)]
x=np.matrix(df3[['R/I','HS','Avrg','SR','50/I','6+4/BF']])
result=model.predict(x)
df3['Class']=pd.DataFrame(result)

df3.to_csv("op.csv")

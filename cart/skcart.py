import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
Location=r'C:\Users\kiran\Desktop\batsman\cart\TrainDataSet.csv'

df=pd.read_csv(Location)



model = DecisionTreeClassifier(criterion='gini')
model.fit(df[['HS','Avg','SR','50/I','6+4/BF']],df['Class'])
print(model)
tree.export_graphviz(model,out_file='result_gini.dot')
Location =r'C:\Users\kiran\Desktop\batsman\cart\TestDataSet.csv'
df3 = pd.read_csv(Location)
df3['Class']='NA'
df3['rating']='0'
df3 = df3[(df3['Inns']>=10)]
x=np.matrix(df3[['HS','Avrg','SR','50/I','6+4/BF']])
result=model.predict(x)

df3['Class']=pd.DataFrame(result)

#df3.to_csv("op.csv")

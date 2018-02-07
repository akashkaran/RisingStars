import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
Location=r'C:\Users\kiran\Desktop\RisingStars\Scikit_Models\cart\exptrain.csv'

df=pd.read_csv(Location)



model = DecisionTreeClassifier(criterion='entropy')
model.fit(df[['R/I','HS','Avrg','SR','50/I','6+4/BF']],df['Class'])
print(model)
tree.export_graphviz(model,out_file='result_entropy.dot')
Location =r'C:\Users\kiran\Desktop\RisingStars\Scikit_Models\cart\TestDataSet.csv'
df3 = pd.read_csv(Location)
df3['Class']='NA'
df3['rating']='0'
df3 = df3[(df3['Inns']>=10)]
x=np.matrix(df3[['R/I','HS','Avrg','SR','50/I','6+4/BF']])
result=model.predict(x)

df3['Class']=pd.DataFrame(result)

df3.to_csv("op.csv")

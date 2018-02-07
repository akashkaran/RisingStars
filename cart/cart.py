import pandas as pd
from math import log
Location = r'C:\Users\kiran\Desktop\RisingStars\cart\exptrain.csv'
df = pd.read_csv(Location)
#taking only feature columns and class column in dataframe
df=df[['R/I','HS','Avrg','SR','50/I','6+4/BF','Class']]

#dataframe to 2d array conversion
data = df.as_matrix(columns=None)
print("________printing sample data__________")
print(data[:10])
'''
for each row in data=>
row[0]=id    row[1]=player row[2]=Span   row[3]=Years row[4]=Inns
row[5]=R/I   row[6]=HS     row[7]=Avrg   row[8]=SR    row[9]=100/I
row[10]=50/I row[11]=BPBF  row[12]=Class
'''
def divideset(rows,column,value):
    split_function=lambda row:row[column]>=value
    set1=[row for row in rows if split_function(row)]
    set2=[row for row in rows if not split_function(row)]
    return (set1,set2)

data1,data2=divideset(data,4,72.93)
'''print(data1)
print(data2)
'''

def uniquecounts(rows):
    results={}
    for row in rows:
        r=row[len(row)-1]
        if r not in results: results[r]=0
        results[r]+=1
    return results

#print(uniquecounts(data))

def entropy(rows):
    log2=lambda x:log(x)/log(2)
    results=uniquecounts(rows)
    ent=0.0
    for r in results.keys():
        p=float(results[r])/len(rows)
        ent=ent-p*log2(p)
    return ent

'''print(entropy(data))
print(entropy(data1))
print(entropy(data2))'''

class decisionnode:
    def __init__(self,col=-1,value=None,results=None,tb=None,fb=None):
        self.col=col
        self.value=value
        self.results=results
        self.tb=tb
        self.fb=fb
        print(("Column is %s, value is %s")%(self.col,self.value,))
        

def buildtree(rows):
    if len(rows)==0:
        return decisionnode()
    
    current_score=entropy(rows)
    best_gain=0.0
    best_criteria=None
    best_sets=None
    #col_count returns total number of features
    col_count=len(rows[0])-1

    for col in range(0,col_count):
        #col_values contains list of all possible values for that column
        global col_values
        col_values={}
        for row in rows:
            col_values[row[col]]=1

        #for loop to divide dataset on each value for the same column and choosing best value for split, best child sets splitted on that value
        for value in col_values.keys():
            #spliting data on value
            set1,set2=divideset(rows,col,value)
            #calculating infromation gain using entropy
            p=float(len(set1))/len(rows)
            gain=current_score-p*entropy(set1)-(1-p)*entropy(set2)
            if gain>best_gain and len(set1)>0 and len(set2)>0:
                best_gain=gain
                best_criteria=(col,value)
                best_sets=(set1,set2)
                print("gain")
                print(gain)
                print("best criteria")
                print(best_criteria)

    print("for loop end for column")


    #create the branches
    if best_gain>0:
        trueBranch=buildtree(best_sets[0])
        falseBranch=buildtree(best_sets[1])
        print("returning node")
        return decisionnode(col=best_criteria[0],value=best_criteria[1],tb=trueBranch,fb=falseBranch)
    else:
        print("returning leaf")
        return decisionnode(results=uniquecounts(rows))

cart=buildtree(data)
#print tree

def printtree(tree,indent=''):
   # Is this a leaf node?
    if tree.results!=None:
        print(str(tree.results))
    else:
        print(str(tree.col)+':'+str(tree.value)+'? ')
        # Print the branches
        print(indent+'T->', end=" ")
        printtree(tree.tb,indent+'  ')
        print(indent+'F->', end=" ")
        printtree(tree.fb,indent+'  ')
        
#classify new data
def classify(testdata,tree):
    if tree.results!=None:
        return tree.results
    else:
        val=testdata[tree.col]
        branch=None
        if val>=tree.value:
            branch=tree.tb
        else:
            branch=tree.fb
        return classify(testdata,branch)


Location= r'C:\Users\kiran\Desktop\RisingStars\cart\TestDataset.csv'
df2 = pd.read_csv(Location)
printtree(cart)
#df2 = df2[['R/I','HS','Avrg','SR','50/I','6+4/BF','Class']]
for index,row in df2.iterrows():
    value=classify([row['R/I'],row['HS'],row['Avrg'],row['SR'],row['50/I'],row['6+4/BF']],cart)
    for key in value:
        df2.loc[index,'Class']=key


#df2.to_csv("output.csv")

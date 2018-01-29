import pickle

# Read the CSV into a pandas data frame (df)
#   With a df you can do many things
#   most important: visualize data with Seaborn
fo=open("csv/icctop100.csv","r")
icc=fo.readlines()
for i in icc:
    ic=i.split(',')
    rank=ic[0].strip()
    name=ic[2].strip()
    #print(rank,name)
fo.close()

fo=open("csv/naive.csv","r")
naive=fo.readlines()
for i in naive:
    na=i.split(',')
    rank=na[0].strip()
    name=na[2].strip()
    #print(rank,name)
fo.close()

fo=open("csv/cart.csv","r")
cart=fo.readlines()
for i in cart:
    ca=i.split(',')
    rank=ca[0].strip()
    name=ca[2].strip()
    #print(rank,name)
fo.close()
i_n=[]
rank=-1
for o in icc:
    ic=o.split(',')
    name=ic[2].strip()

    s="";
    for s in naive:
        if (name in s):
            rank=rank+1
            #print(name,rank,s.split(',')[0])
            st=name+","+str(rank)+","+str(s.split(',')[0])
            i_n.append(st)
#print(i_n)
ovr=[]
fop=open('result.csv','w+')
for o in i_n:
    ic=o.split(',')
    #print(ic)
    name=ic[0].strip()
    rank=ic[1]
    naive=ic[2]
    s="" 
    for s in cart:
        if (name in s):
            print(name,rank,naive,s.split(',')[0])
            st1=name+","+str(rank)+","+str(naive)+","+str(s.split(',')[0])+"\n"
            ovr.append(st1)
            fop.write(st1)



# Or export it in many ways, e.g. a list of tuples
#tuples = [tuple(x) for x in df.values]

# or export it as a list of dicts
#dicts = df.to_dict().values()


# 

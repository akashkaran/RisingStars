from source.k import *

icc=readIcc()
nblist=readNb()
fop=open('csv/icc_naive.csv','w+') #Backup
icc_nb=[]                          #Relative ranking List
rank=0
for o in icc:
    ic=o.split(',')
    ic_rank=ic[0].strip()
    name=ic[2].strip()
    s="";
    inc=11
    for inc,s in enumerate(nblist):
        if (name in s):
            rank=rank+1
            #ICC name     icc Rank   rel_rank        nb Rank      
            st=name+"  ("+ic_rank+"),"+str(rank)+","+str(s.split(',')[0])+"\n"
            icc_nb.append(st)
            fop.write(st)
            print(st)
fop.close()

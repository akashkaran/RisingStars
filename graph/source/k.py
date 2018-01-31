import re
import sys
import csv
import json

def readIcc():
    fo_icc=open("csv/icctop100.csv","r")
    icc=fo_icc.readlines()

    '''
    for i in icc:
        ic=i.split(',')
        ic_rank=ic[0].strip()
        ic_name=ic[2].strip()
        #print(ic_rank,ic_name)
    '''
    fo_icc.close()
    return icc

def readNb():
    #nb List
    fo_naive=open("csv/nbresult.csv","r")
    naive=fo_naive.readlines()
    nbr=0
    nblist=[]
    for i in naive:
        na=i.split(',')
        nb_rank=nbr
        nb_name=re.sub(re.compile("\((.*?)\)"), '', na[2].strip())
        #print(nb_rank,nb_name)
        nbstr=str(nb_rank)+","+nb_name
        nblist.append(nbstr)
        nbr+=1    
    fo_naive.close()
    return nblist

def readCart():
    #cart List
    car=0
    calist=[]
    fo_cart=open("csv/cartresult.csv","r")
    cart=fo_cart.readlines()
    for i in cart:
        ca=i.split(',')
        ca_rank=car
        ca_name=re.sub(re.compile("\((.*?)\)"), '', ca[2].strip())
        castr=str(ca_rank)+","+ca_name
        calist.append(castr)
        car+=1
    fo_cart.close()
    return calist
    
#Merging Icc nb and cart ranks into single list
def merge(icc,nblist,calist):
    i_n=[]
    rank=0
    for o in icc:
        ic=o.split(',')
        name=ic[2].strip()
        s="";
        for s in nblist:
            if (name in s):
                rank=rank+1
                #print(name,rank,s.split(',')[0])
                st=name+","+str(rank)+","+str(s.split(',')[0])
                i_n.append(st)
    #print(i_n)
    ovr=[]
    fop=open('source/graph_ip.csv','w+')
    for o in i_n:
        ic=o.split(',')
        #print(ic)
        name=ic[0].strip()
        rank=ic[1]
        naive=ic[2]
        s="" 
        for s in calist:
            if (name in s):
                print(name,rank,naive,s.split(',')[0])
                #ICC name       rel_rank       nb Rank           cart rank
                st1=name+","+str(rank)+","+str(naive)+","+str(s.split(',')[0])+"\n"
                ovr.append(st1)
                fop.write(st1)

# to convert into json for graph input
def convert(result):
  csv_filename = "source/graph_ip.csv"
  fieldnames=["name","icc","naive","cart"]
  print ("Opening CSV file: "+csv_filename)
  f=open(csv_filename, 'r')
  csv_reader = csv.DictReader(f,fieldnames)
  json_filename = csv_filename.split(".")[0]+".js"
  print("Saving JSON to file: "+json_filename)
  jsonf = open(json_filename,'w')
  stvar="var jsonfile={jsonarray:"
  end="};"
  data = json.dumps([r for r in csv_reader])
  jsonf.write(stvar)
  jsonf.write(data)
  jsonf.write(end)
  f.close()
  jsonf.close()
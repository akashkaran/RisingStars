'''pattern = re.compile('\W')
	pl_name = re.sub(re.compile('\W'), '', pl_name)
'''
import re
#Rank Merging
fo_icc=open("csv/icctop100.csv","r")
icc=fo_icc.readlines()
#dict_icc={}
#dict_na={}
#dict_ca={}
for i in icc:
    ic=i.split(',')
    ic_rank=ic[0].strip()
    ic_name=ic[2].strip()
    #dict_icc[ic_rank]=ic_name
    #print(ic_rank,ic_name)
fo_icc.close()
#print(dict_icc.items())

fo_naive=open("csv/naive.csv","r")
naive=fo_naive.readlines()
for i in naive:
    na=i.split(',')
    na_rank=na[0].strip()
    na_name=na[2].strip()
    na[2] = re.sub(re.compile("\((.*?)\)"), '', na_name)
    print(na_rank,na_name)
    #dict_na[na_rank]=na_name
fo_naive.close()
#print("\nNaive\n")
#print(dict_na.items())

fo_cart=open("csv/cart.csv","r")
cart=fo_cart.readlines()
for i in cart:
    ca=i.split(',')
    ca_rank=ca[0].strip()
    ca_name=ca[2].strip()
    #print(rank,name)
    #dict_ca[ca_rank]=ca_name
fo_cart.close()

#for i in icc:


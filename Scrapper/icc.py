
#<table class="top100table" cellspacing="0" cellpadding="0">
import requests
import os
from bs4 import BeautifulSoup
request=requests.get("http://www.relianceiccrankings.com/ranking/odi/batting/")
content=request.content
soup=BeautifulSoup(content, "html.parser")
print("Data Parsing...")
csv="icctop100.csv"
file = open(os.path.expanduser(csv),"wb")
header="Rank,Rating,Name\n"
file.write(bytes(header,encoding="ascii",errors='ignore'))
pls=soup.find("table",{"class":"top100table"})
#print(pls)
trdata=pls.findAll('tr')
s="";
inx=7;
for inx,rec in enumerate(trdata):
    i=0;
    for tx in rec.findAll('td'):
        s="\n";tdtxt="";
        i=i+1;
        tdtxt=tx.text.replace('\n','').replace('\t','').replace('*','') 
        if i==1 or i==2 or i==3:
            tdtxt=tdtxt+","
        else:
            tdtxt=""
        #print(tdtxt)
        if tdtxt==",":
            continue
        file.write(bytes(tdtxt,encoding="ascii",errors='ignore'))
    if tdtxt==",":
        continue
    file.write(bytes(s,encoding="ascii",errors='ignore'))
print("Imported to "+csv+"!")

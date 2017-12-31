import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
import re
def make_soup(url):
        thepage = urllib.request.urlopen(url)
        soupdata = BeautifulSoup(thepage, "html.parser")
        print("Parsing...")
        return soupdata


csv="All_Players.csv"
file = open(os.path.expanduser(csv),"wb")
header="Player,Span,Mat,Inns,NO,Runs,R/I,HS,Ave,BF,SR,100,50,0,4s,6s"+"\n"
file.write(bytes(header,encoding="ascii",errors='ignore'))
pg=1;
for pg in range(1,7):   #Page Iterations
        list_pl = make_soup("http://stats.espncricinfo.com/ci/engine/stats/index.html?agemax2=28;agemin2=22;ageval2=age;class=2;filter=advanced;orderby=runs;page="+str(pg)+";spanmax2=15+Dec+2017;spanmin2=15+Dec+2013;spanval2=span;team=1;team=12;team=15;team=2;team=25;team=29;team=3;team=4;team=40;team=5;team=6;team=7;team=8;team=9;template=results;type=batting;wrappertype=print")
        tdata=list_pl.findAll("table",{"class":"engineTable"})
        cdata=tdata[2]  #main Table data
        ldata=cdata.findAll("tr",{"class":"data1"})
        s="\n"
        print("** Data Parsed Page "+str(pg)+" **")
        for record in ldata:
                k=""
                i=0;
                for data in record.findAll('td'):
                        k=data.text.replace('\n','').replace('\t','').replace('*','')
                        i=i+1;
                        if i == 4:
                                t=int(k)
                        elif i == 6:
                                ty=int(k)/t
                                k=k+","+str(ty) #for R/I column
                        k=k+","
                        file.write(bytes(k,encoding="ascii",errors='ignore'))
                file.write(bytes(s,encoding="ascii",errors='ignore'))
print("Imported to "+csv+"!")







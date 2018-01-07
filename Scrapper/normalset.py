#Normal set 1+Jan+2015 to 31+Dec+2017

#http://stats.espncricinfo.com/ci/engine/stats/index.html?agemax1=23;agemin1=20;ageval1=age;class=2;filter=advanced;orderby=runs;spanmax1=31+Dec+2016;spanmin1=1+Jan+2001;spanval1=span;template=results;type=batting;wrappertype=print
#http://stats.espncricinfo.com/ci/engine/stats/index.html?agemax1=24;agemin1=21;ageval1=age;class=2;filter=advanced;orderby=runs;spanmax1=31+Dec+2016;spanmin1=1+Jan+2001;spanval1=span;template=results;type=batting;wrappertype=print
#http://stats.espncricinfo.com/ci/engine/stats/index.html?agemax1=25;agemin1=22;ageval1=age;class=2;filter=advanced;orderby=runs;spanmax1=31+Dec+2016;spanmin1=1+Jan+2001;spanval1=span;template=results;type=batting;wrappertype=print
#http://stats.espncricinfo.com/ci/engine/stats/index.html?agemax1=26;agemin1=23;ageval1=age;class=2;filter=advanced;orderby=runs;spanmax1=31+Dec+2016;spanmin1=1+Jan+2001;spanval1=span;template=results;type=batting;wrappertype=print


import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
import re
import pickle
def make_soup(url):
        thepage = urllib.request.urlopen(url)
        soupdata = BeautifulSoup(thepage, "html.parser")
        print("Parsing...")
        return soupdata
#1      2    3   4    5   6   7   8   9  10  11  12  13  14  15
#Player,Span,Mat,Inns,NO,Runs,HS,Ave,BF ,SR, 100,50, 0,  4s, 6s
csv="TestingSet.csv"
file = open(os.path.expanduser(csv),"wb")
header="Player,Span,Years,Inns,R/I,HS,Avg,SR,100/I,50/I,6+4/BF"+"\n"
file.write(bytes(header,encoding="ascii",errors='ignore'))
substr=";spanmax1=31+Dec+2017;spanmin1=1+Jan+2014;spanval1=span;template=results;type=batting;wrappertype=print";                       #1+Jan+2014 to 31+Dec+2017
lisp=["http://stats.espncricinfo.com/ci/engine/stats/index.html?agemax1=24;agemin1=20;ageval1=age;class=2;filter=advanced;orderby=runs;"];
pl_tab=[];
o=0;
for pgs in lisp:
        pg=1;o=o+1;
        for pg in range(1,4):   #Page Iterations
                list_pl = make_soup(pgs+"page="+str(pg)+substr);
                #print(pgs)
                tdata=list_pl.findAll("table",{"class":"engineTable"})
                cdata=tdata[2]  #main Table data
                ldata=cdata.findAll("tr",{"class":"data1"})
                s="\n"
                print("** Data Parsed Page "+str(pg)+" Link "+str(o)+" **")
                for record in ldata:
                        kq="";kq1="";
                        list1=record.findAll('td')
                        pl=list1[0].text.replace('\n','').replace('\t','').replace('*','')
                        kq=list1[1].text.replace('\n','').replace('\t','').replace('*','')
                        x1=int(kq.split("-")[0])
                        x2=int(kq.split("-")[1])
                        sp=x2-x1+1
                        kq1=list1[3].text.replace('\n','').replace('\t','').replace('*','')
                        inn = int(kq1)
                        if sp >= 3 and inn >= 10:
                                with open('pltable','rb') as fp:
                                        pltab=pickle.load(fp)
                                if any(pl in s for s in pltab):
                                    continue
                                else:
                                    pl_tab.append(pl);
                                    k="";
                                    i=0;bnd=0;no=0;hun=0;fif=0;t=0;bf=0;
                                    for data in record.findAll('td'):
                                            k=data.text.replace('\n','').replace('\t','').replace('*','')
                                            i=i+1;
                                            k=k+","
                                            file.write(bytes(k,encoding="ascii",errors='ignore'))
                                    file.write(bytes(s,encoding="ascii",errors='ignore'))
print(pl_tab)
print("Imported to "+csv+"!")







#Training Set 1+Jan+2001 to 31+Dec+2013

#http://stats.espncricinfo.com/ci/engine/stats/index.html?agemax1=23;agemin1=20;ageval1=age;class=2;filter=advanced;opposition=1;orderby=runs;spanmax1=31+Dec+2016;spanmin1=1+Jan+2001;spanval1=span;template=results;type=batting
#http://stats.espncricinfo.com/ci/engine/stats/index.html?agemax1=24;agemin1=21;ageval1=age;class=2;filter=advanced;opposition=2orderby=runs;spanmax1=31+Dec+2016;spanmin1=1+Jan+2001;spanval1=span;template=results;type=batting;wrappertype=print
#http://stats.espncricinfo.com/ci/engine/stats/index.html?agemax1=25;agemin1=22;ageval1=age;class=2;filter=advanced;opposition=2orderby=runs;spanmax1=31+Dec+2016;spanmin1=1+Jan+2001;spanval1=span;template=results;type=batting;wrappertype=print
#http://stats.espncricinfo.com/ci/engine/stats/index.html?agemax1=26;agemin1=23;ageval1=age;class=2;filter=advanced;opposition=2orderby=runs;spanmax1=31+Dec+2016;spanmin1=1+Jan+2001;spanval1=span;template=results;type=batting;wrappertype=print
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
#opposition Teams
print("\n 40  Afghanistan\
\n 4058 Africa XI \
\n 106Asia XI\
\n 25 Bangladesh\
\n 12 Bermuda\
\n 17 Canada\
\n 14 East Africa\
\n 1  England\
\n 19 Hong Kong\
\n 140ICC World XI\
\n 6  India\
\n 29 Ireland\
\n 26 Kenya\
\n 28 Namibia\
\n 15 Netherlands\
\n 5  New Zealand\
\n 7  Pakistan\
\n 20 Papua New Guinea\
\n 30 Scotland\
\n 3  South Africa\
\n 8  Sri Lanka\
\n 27 United Arab Emirates\
\n 11 United States of America\
\n 4  West Indies<\
\n 9  Zimbabwe")
substr=";spanmax1=31+Dec+2013;spanmin1=1+Jan+2001;spanval1=span;template=results;type=batting;wrappertype=print";                       #1+Jan+2001 to 31+Dec+2013
lisp=["http://stats.espncricinfo.com/ci/engine/stats/index.html?agemax1=23;agemin1=20;ageval1=age;class=2;filter=advanced;opposition=",
      "http://stats.espncricinfo.com/ci/engine/stats/index.html?agemax1=24;agemin1=21;ageval1=age;class=2;filter=advanced;opposition=",
      "http://stats.espncricinfo.com/ci/engine/stats/index.html?agemax1=25;agemin1=22;ageval1=age;class=2;filter=advanced;opposition=",
      "http://stats.espncricinfo.com/ci/engine/stats/index.html?agemax1=26;agemin1=23;ageval1=age;class=2;filter=advanced;opposition="];
pl_tab=[];
flag=0;
o=0;
op=str(input("Enter opp no:")) #select the opposition team from above menu
for pgs in lisp:
        pg=1;o=o+1;
        for pg in range(1,3):   #Page Iterations
                list_pl = make_soup(pgs+op+";orderby=runs;"+"page="+str(pg)+substr);
                #print(pgs)
                tdata=list_pl.findAll("table",{"class":"engineTable"})
                team=tdata[0]
                tname=team.findAll("td",{"class":"left"})
                #name of csv
                opp=tname[1].text[17:].replace(" ","").replace('\n','').replace('\t','')
                print(opp)
                #creating csv file
                if flag==0:
                    csv="trainingOpp/"+opp+".csv"
                    file = open(os.path.expanduser(csv),"wb")
                    header="Player,Span,Years,Inns,R/I,HS,Avg,SR,100/I,50,50/I,4,6,6+4/BF"+"\n"
                    file.write(bytes(header,encoding="ascii",errors='ignore'))
                    flag=1;
                
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
                        kq1=list1[3].text.replace('\n','').replace('\t','').replace('*','').replace('-','')
                        inn = int(kq1)
                        if sp >= 3 and inn >= 10:
                                pattern = re.compile("\((.*?)\)")
                                pl = re.sub(pattern, '', pl)
                                if any(pl in s for s in pl_tab):
                                    continue
                                else:
                                    pl_tab.append(pl);
                                    #print(pl)
                                    k="";
                                    i=0;bnd=0;no=0;hun=0;fif=0;t=0;bf=0;fl=0;
                                    for data in record.findAll('td'):
                                            k=data.text.replace('\n','').replace('\t','').replace('*','') 
                                            i=i+1;
                                            if i==1 :                  #1 Player
                                                    k=k+","
                                            elif i==2 :                #2 Span,Years
                                                    x1=int(k.split("-")[0])
                                                    x2=int(k.split("-")[1])
                                                    sp=x2-x1+1
                                                    k=k+","+str(sp)+","
                                            elif i == 4:               #3 Inns
                                                    t=int(k)
                                                    k=k+","
                                            #elif i == 5:               # No/I
                                            #        no=int(k)/t
                                            #        k=str(no)+","
                                            elif i == 6:               #4 R/I
                                                    ty=int(k)/t
                                                    k=str(ty)+","
                                            elif i == 7:               #5 HS
                                                    k=k+","
                                            elif i == 8:               #6 Avg
                                                    k=k+","
                                            elif i == 9:
                                                    bf=int(k)
                                                    k=""
                                            elif i == 10:              #7 SR
                                                    k=k+","
                                            elif i == 11:              #8 100/I
                                                    hun=int(k)/t
                                                    k=str(hun)+","
                                            elif i == 12:              #9 50/I
                                                    fif=int(k)/t
                                                    k=k+","+str(fif)+","
                                            elif i == 14:
                                                    bnd=int(k)
                                                    k=k+","
                                            elif i == 15:                   
                                                    bnd=bnd+int(k)     #10 6+4/BF
                                                    bnd=bnd/bf 
                                                    k=k+","+str(bnd)
                                            else:
                                                    k=""
                                            file.write(bytes(k,encoding="ascii",errors='ignore'))
                                    file.write(bytes(s,encoding="ascii",errors='ignore'))
print(pl_tab)
with open('pltable','wb') as fp:
        pickle.dump(pl_tab,fp)
print("Imported to "+csv+"!")







#http://stats.espncricinfo.com/ci/engine/stats/index.html?batting_positionmax1=7;batting_positionval1=batting_position;class=21;filter=advanced;orderby=runs;size=50;spanmin1=1+Jan+2014;spanval1=span;template=results;type=batting;wrappertype=print

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

#1      2    3   4    5   6   7   8   9  10  11  12  13  14  15
#Player,Span,Mat,Inns,NO,Runs,HS,Ave,BF ,SR, 100,50, 0,  4s, 6s
csv="U19Testing_data.csv"9
file = open(os.path.expanduser(csv),"wb")
#       1       2   3    4   5   6  7     8    9
header="Player,Inns,NO/I,R/I,Avg,SR,100/I,50/I,6+4/BF"+"\n"
file.write(bytes(header,encoding="ascii",errors='ignore'))
pg=1;
for pg in range(1,11):   #Page Iterations
        list_pl = make_soup("http://stats.espncricinfo.com/ci/engine/stats/index.html?batting_positionmax1=7;"+
                            "batting_positionval1=batting_position;class=21;filter=advanced;orderby=runs;page="+str(pg)+";"+
                            "size=50;spanmin1=1+Jan+2014;spanval1=span;template=results;type=batting;wrappertype=print")
        tdata=list_pl.findAll("table",{"class":"engineTable"})
        cdata=tdata[2]  #main Table data
        ldata=cdata.findAll("tr",{"class":"data1"})
        s="\n"
        print("** Data Parsed Page "+str(pg)+" **")
        for record in ldata:
                kq="";
                list1=record.findAll('td')
                kq=list1[3].text.replace('\n','').replace('\t','').replace('*','')
                inn = int(kq)
                if inn > 9 :                   #innings gt 
                        k="";
                        i=0;bnd=0;no=0;hun=0;fif=0;t=0;bf=0;
                        for data in record.findAll('td'):
                                k=data.text.replace('\n','').replace('\t','').replace('*','')
                                i=i+1;
                                if i==1 :          #1 Player
                                        k=k+","
                                elif i == 4:               #2 Inns
                                        t=int(k)
                                        k=k+","
                                elif i == 5:               #3 No/I
                                        no=int(k)/t
                                        k=str(no)+","
                                elif i == 6:               #4 R/I
                                        ty=int(k)/t
                                        k=str(ty)+","
                                elif i == 8:               #5 Avg
                                        k=k+","
                                elif i == 9:
                                        bf=int(k)
                                        k=""
                                elif i == 10:              #6 SR
                                        k=k+","
                                elif i == 11:              #7 100/I
                                        hun=int(k)/t
                                        k=str(hun)+","
                                elif i == 12:              #8 50/I
                                        fif=int(k)/t
                                        k=str(fif)+","
                                elif i == 14:
                                        bnd=int(k)
                                        k=""
                                elif i == 15:                   
                                        bnd=bnd+int(k)     #9 6+4/BF
                                        bnd=bnd/bf 
                                        k=str(bnd)
                                else:
                                        k=""
                                file.write(bytes(k,encoding="ascii",errors='ignore'))
                        file.write(bytes(s,encoding="ascii",errors='ignore'))
print("Imported to "+csv+"!")







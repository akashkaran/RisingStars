#Testing set 1+Jan+2014 to 31+Dec+2017
#http://stats.espncricinfo.com/ci/engine/stats/index.html?agemax1=24;agemin1=20;ageval1=age;page=no;bowling_positionmax1=4;bowling_positionmin1=1;bowling_positionval1=bowling_position;class=2;filter=advanced;orderby=wickets;spanmax1=31+Dec+2017;spanmin1=01+Jan+2014;spanval1=span;template=results;type=bowling;wrappertype=print

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
#1      2    3   4    5      6     7    8     9    10  11    12 13  14 
#Player Span Mat Inns Overs  Mdns  Runs Wkts  BBI  Ave Econ  SR  4   5
csv="TestingSetB.csv"
file = open(os.path.expanduser(csv),"wb")
header="Player,Span,Years,Inns,Overs,Mdns/Ove,Runs,Wkts,BBI,Ave,Econ"+"\n"
file.write(bytes(header,encoding="ascii",errors='ignore'))
substr1=";bowling_positionmax1=4;bowling_positionmin1=1;bowling_positionval1=bowling_position;class=2;filter=advanced;orderby=wickets;"
substr2="spanmax1=31+Dec+2017;spanmin1=01+Jan+2014;spanval1=span;template=results;type=bowling;wrappertype=print";                       #1+Jan+2014 to 31+Dec+2017
lisp=["http://stats.espncricinfo.com/ci/engine/stats/index.html?agemax1=26;agemin1=20;ageval1=age;"];
bw_tab=[];
o=0;ct=0;
for pgs in lisp:
        pg=1;o=o+1;
        for pg in range(1,10):   #Page Iterations
                try:
                        list_pl = make_soup(pgs+"page="+str(pg)+substr1+substr2);
                        #print(pgs+"page="+str(pg)+substr1+substr2)
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
                                if sp >= 2 and inn >= 10:    
                                        pattern = re.compile("\((.*?)\)")
                                        pl = re.sub(pattern, '', pl)
                                        if any(pl in s for s in bw_tab):
                                            continue
                                        else:
                                            bw_tab.append(pl);
                                            print(pl)
                                            ct+=1
                                            k="";
                                            i=0;mdn=0.0;ovr=0.0;bf1=0.0;bf2=0.0;bf=0.0;ovr=0.0;
                                            for data in record.findAll('td'):
                                                    k=data.text.replace('\n','').replace('\t','').replace('*','') 
                                                    i=i+1;
                                                    if i==1 :                  #1 Player
                                                            k=k+","
                                                    elif i==2 :                #2 Span, #3Years
                                                            x1=int(k.split("-")[0])
                                                            x2=int(k.split("-")[1])
                                                            sp=x2-x1+1
                                                            k=k+","+str(sp)+","
                                                    elif i == 4:               #4 Inns
                                                            k=k+","
                                                    elif i == 5:              #5 Ovr
                                                            ovr=float(k)
                                                            k=str(ovr)+","
                                                    elif i == 6:               #6 Mdns
                                                            mdn=float(k)
                                                            mdn=mdn/ovr
                                                            k=str(mdn)+","
                                                    elif i == 7:               #7 Runs
                                                            k=k+","
                                                    elif i == 8:               #8 WKTS
                                                            k=k+","
                                                    elif i == 9:               #9 BBI
                                                            bf1=float(k[0:1])
                                                            bf2=float(k[2:])
                                                            bf=bf1/bf2
                                                            k=str(bf)+","
                                                    elif i == 10:              #10  Ave         
                                                            k=k+","
                                                    elif i == 11:              #11 Econ
                                                            k=k+","
                                                    else:
                                                            k=""
                                                    file.write(bytes(k,encoding="ascii",errors='ignore'))
                                            file.write(bytes(s,encoding="ascii",errors='ignore'))
                except IndexError:
                        print("pages exhausted! or Net gela")
                        break
#print(bw_tab)
with open("bw.tmp",'wb') as fp:
        pickle.dump(bw_tab,fp)
print("total count: "+str(ct))
print("Imported to "+csv+"!")







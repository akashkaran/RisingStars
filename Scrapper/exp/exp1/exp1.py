#link http://stats.espncricinfo.com/ci/engine/stats/index.html?agemax1=24;agemin1=20;ageval1=age;batting_positionmax1=5;batting_positionval1=batting_position;class=2;filter=advanced;orderby=runs;template=results;type=batting
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
csv="exp1.csv"
file = open(os.path.expanduser(csv),"wb")
header="Player,Span,Years,Inns,R/I,HS,Avg,SR,100/I,50/I"+"\n"
file.write(bytes(header,encoding="ascii",errors='ignore'))
substr=";template=results;type=batting;wrappertype=print";                       
lisp=["http://stats.espncricinfo.com/ci/engine/stats/index.html?agemax1=23;agemin1=20;ageval1=age;batting_positionmax1=5;batting_positionval1=batting_position;class=2;filter=advanced;orderby=runs;",
      "http://stats.espncricinfo.com/ci/engine/stats/index.html?agemax1=24;agemin1=21;ageval1=age;batting_positionmax1=5;batting_positionval1=batting_position;class=2;filter=advanced;orderby=runs;",
      "http://stats.espncricinfo.com/ci/engine/stats/index.html?agemax1=25;agemin1=22;ageval1=age;batting_positionmax1=5;batting_positionval1=batting_position;class=2;filter=advanced;orderby=runs;",
      "http://stats.espncricinfo.com/ci/engine/stats/index.html?agemax1=26;agemin1=23;ageval1=age;batting_positionmax1=5;batting_positionval1=batting_position;class=2;filter=advanced;orderby=runs;"];
pl_tab=[];
o=0;ct=0;
for pgs in lisp:
        pg=1;o=o+1;
        for pg in range(1,11):   #Page Iterations
                try:
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
                                        pattern = re.compile("\((.*?)\)")
                                        pl = re.sub(pattern, '', pl)
                                        if any(pl in s for s in pl_tab):
                                            continue
                                        else:
                                            pl_tab.append(pl);
                                            #print(pl)
                                            ct+=1
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
                                                            k=str(fif)+","
                                                    elif i == 14:
                                                            bnd=int(k)
                                                            k=""
                                                    #elif i == 15:                   
                                                     #       bnd=bnd+int(k)     #10 6+4/BF
                                                     #       bnd=bnd/bf 
                                                     #       k=str(bnd)
                                                    else:
                                                            k=""
                                                    file.write(bytes(k,encoding="ascii",errors='ignore'))
                                            file.write(bytes(s,encoding="ascii",errors='ignore'))
                except ValueError:
                        print("pages exhausted!")
print(pl_tab)
with open("pl.tmp",'wb') as fp:
        pickle.dump(pl_tab,fp)
print("total count: "+str(ct))
print("Imported to "+csv+"!")







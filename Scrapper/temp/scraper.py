import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
import re
def make_soup(url):
	thepage = urllib.request.urlopen(url)
	soupdata = BeautifulSoup(thepage, "html.parser")
	return soupdata


list_pl = make_soup("http://www.espncricinfo.com/india/content/player")
pl_href=list_pl.findAll("table",{"class":"playersTable"})
hrefx=pl_href[0]
pld=[]
i=0
pl_refs=hrefx.findAll('a')
for pl in pl_refs:
	hrs=pl.get('href').replace('/ci','')
	pld.append(hrs)
	print(i)
	i=i+1




for hr in range(0,len(pld)):
	linkx="http://www.espncricinfo.com/india"+pld[hr]
	print(linkx)
	
for hr in pld:
	linkx="http://www.espncricinfo.com/india"+hr
	soup = make_soup(linkx)
	pl_nam=soup.find("div",{"class":"ciPlayernametxt"})
	pl_name=pl_nam.find('h1').text
	pattern = re.compile('\W')
	pl_name = re.sub(pattern, '', pl_name)
	csv=pl_name+".csv"
	file = open(os.path.expanduser(csv),"wb")
	header="  ,Mat,Inns,NO,Runs,HS,Ave,BF,SR,100,50,4s,6s,Ct,St"+"\n"
	file.write(bytes(header,encoding="ascii",errors='ignore'))
	tdata=soup.findAll("table",{"class":"engineTable"})
	cdata=tdata[0]                                                  #for first table
	pdata=cdata.findAll("tr",{"class":"data1"})
	s="\n"
	for record in pdata:
		k=""
		for data in record.findAll('td'):
			k=data.text.replace('\n','').replace('\t','').replace('*','')
			k=k+","
			file.write(bytes(k,encoding="ascii",errors='ignore'))
		file.write(bytes(s,encoding="ascii",errors='ignore'))







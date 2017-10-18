from urllib.request import urlopen as ureq

from bs4 import BeautifulSoup as soup

import csv

 my_url='http://www.espncricinfo.com/india/content/player/253802.html'


f = csv.writer(open("first.csv", "w"))
f.writerow(["Name"]
 uClient=ureq(my_url)
 page_html=uClient.read()
 uClient.close()
 soup(page_html,"html.parser")
 page_soup=soup(page_html,"html.parser")
 containers=page_soup.findAll("div",{"class":"engineTable"})
 contain=containers[0]

 tds=contain.findAll("tr",{"class":"data1"})


 Matches =  tds[0]
 f.writerow([Matches])
import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
import re
def make_soup(url):
	thepage = urllib.request.urlopen(url)
	soupdata = BeautifulSoup(thepage, "html.parser")
	return soupdata

file = open(os.path.expanduser("list.html"),"wb")

soup = make_soup("http://www.espncricinfo.com/india/content/player")
pl_href=soup.findAll("table",{"class":"playersTable"})
hrefx=pl_href[0]
pl_refs=hrefx.findAll('a')
for pl in pl_refs:
	hr=pl.get('href').replace('/ci','')
	
#!/usr/bin/python
import requests
from bs4 import BeautifulSoup

url="http://hurriyet.com.tr/son-dakika"
r=requests.get(url)
data=r.text
soup=BeautifulSoup(data,"html.parser")
a=soup.prettify()
print len(a)
for tag in soup.find_all("script"):
    tag.clear()
    tag.extract()
a=soup.prettify()
print a
#!/usr/bin/python
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests

def printtags(soup):
    temp=[]
    for tag in soup.find_all(True):
        temp.append(str(tag.name))
    print list(set(temp))
    
def printpage(soup):
    print soup.prettify()
    return printtags(soup)

def userpick():
    t=raw_input("Pick a tag to follow:") 
    return SoupStrainer(t)

def letsoup(selected_tag):
    return BeautifulSoup(data,'html.parser',parse_only=selected_tag)


url='http://ikcu.edu.tr/Duyuru'
r=requests.get(url)
data=r.text
soup=BeautifulSoup(data,'html.parser')
printpage(soup)
selected_tag=userpick()
newsoup=letsoup(selected_tag)
printpage(newsoup)
pickorgo=raw_input("Wanna pick more tags?y/n:")
if pickorgo=='y':
    sel_tag=userpick()
    newsoup=letsoup(sel_tag)
elif pickorgo=='n':
    raw_input("kopkop")
else:
    sys.exit()
printpage(newsoup)

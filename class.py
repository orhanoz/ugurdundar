import requests
from bs4 import BeautifulSoup

url="http://ikcu.edu.tr/Duyuru"
class ugur():
    def get(self):
        r=requests.get(url)
        data=r.text
        self.soup=BeautifulSoup(data,"html.parser")
    def removetags(self,soup,tagname):
        for tag in soup.find_all(tagname):
            tag.clear()
            tag.extract()
        print("Tag removed.")
    def printcontain(self,soup,tagname):
        for tag in soup.find_all(tagname):
            print tag.prettify()
    def printtags(self,soup):
        tagz=[]
        for tag in soup.find_all(True):
            tagz.append(str(tag.name))
        print list(set(tagz))
    def selectagname(self):
        tag_sel=raw_input("Tag name:")
        return tag_sel
    def whattodo(self):
        usr_sel=raw_input("Either you can see inside a tag or remove a tag(s/r):")
        if usr_sel=='s':
            return ugur.printcontain(self, x.soup, tagname)
        elif usr_sel=='r':
            return ugur.removetags(self, x.soup, tagname)  
x=ugur()
x.get()
x.removetags(x.soup, "script")
print x.soup.prettify()
x.printtags(x.soup)
tagname=x.selectagname()
x.whattodo()
print x.soup.prettify()



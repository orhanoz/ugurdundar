import requests
from bs4 import BeautifulSoup
import argparse
class U(object):
    pass
u=U()
parser=argparse.ArgumentParser(description="Ugur Dundar will help you extract information from web but only if you help him")
parser.add_argument('-u','--url',nargs=1,default=" ",metavar='foo.com',help="expects an url without http://")
args = parser.parse_args(namespace=u)
if u.url[0]==" ":
    ur=raw_input("Ugur Dundar expects an url without http://\n")
    url='http://'+ur
else:
    url='http://'+u.url[0]
print "Url you provided to Ugur Dundar is %s"%url

#url="http://ikcu.edu.tr/Duyuru"
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
    def whattodo(self,tagname):
        usr_sel=raw_input("You have 3 options:\n<s> for seeing inside the tag\n<r>for removing the tag\n<d> if you are happy with your choice\n(s/r/d):")
        if usr_sel=='s':
            return ugur.printcontain(self, x.soup, tagname)
        elif usr_sel=='r':
            return ugur.removetags(self, x.soup, tagname)
        else:
            print "Wrong key use s for see inside or r for remove...\nNow try again"
            return ugur.whattodo(self,tagname)  


if __name__=='__main__':
    x=ugur()
    x.get()
    clr=raw_input("Do you want Ugur Dundar to clear scripts for you ?? (y/n):")
    if clr=='y':
        x.removetags(x.soup, "script")
    else:
        pass
    
    print x.soup.prettify()
    x.printtags(x.soup)
    tagname=x.selectagname()
    x.whattodo(tagname)
    #print x.soup.prettify()
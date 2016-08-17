import requests,argparse
from bs4 import BeautifulSoup
from time import sleep

class U(object):
    pass
u=U()
parser=argparse.ArgumentParser(description="Ugur Dundar will help you extract information and regularly check for new updates but only if you help him")
parser.add_argument('-u','--url',nargs=1,default=" ",metavar='foo.com',help="expects an url without http://")
args = parser.parse_args(namespace=u)
def greeting():
    print'\n                \033[0;37;41mUgur Dundar Greets You\033[0m'
    print '[0;1;30;40mXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX@[0;5;33;40m@[0;1;30;43m88[0;5;33;40m:[0;1;30;43m8[0;33;47m8[0;1;30;43m88[0;5;33;40m8[0;1;30;41m8[0;1;30;40mXXXXXXXXXXXXXXXXX[0m'
    print '[0;1;30;40mXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX8[0;5;33;40mS[0;33;47m8X[0;1;33;47m@[0;1;31;47m8[0;33;47m8[0;1;31;43m8[0;33;47m8[0;1;31;43m8[0;1;30;43m88@[0;31;40m8[0;1;30;40m8XXXXXXXXXXXXXX[0m'
    print '[0;1;30;40mXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX[0;5;33;40mXt[0;1;31;47m8[0;33;47m8[0;5;37;41m8[0;1;33;47m8[0;1;31;47m@[0;1;33;47m@[0;5;37;41m8[0;33;47m8[0;31;43m8[0;5;33;40mt[0;33;41m8[0;5;31;40mS[0;1;30;40m@XXXXXXXXXXXXXX[0m'
    print '[0;1;30;40m@X@X@@X@X@X@@X@X@@X@@X@X@X@@X@X[0;5;33;40mt[0;37;43m@[0;5;37;41m8[0;1;33;47m8[0;5;33;41mt[0;1;30;47mS[0;1;31;47m8[0;37;43m@[0;5;33;41m;[0;33;47m@8[0;5;33;41m:[0;5;33;40mt[0;5;31;40mS[0;32;40mS[0;1;30;40m8@@X@@X@@X@@X@[0m'
    print '[0;1;30;40m8@88@8888@8@8888@88@8888@88@88[0;5;31;40mX[0;5;33;40mS[0;1;30;43m8[0;1;31;47m8[0;33;47m8@[0;1;33;47m8[0;5;37;41m8[0;33;47m88[0;5;33;41mS[0;33;47m8[0;1;30;43m8@[0;1;30;41m8[0;1;30;40m@8@88@88@88@88@[0m'
    print '[0;1;30;40m88888888888888888888888888888[0;5;36;40m%[0;1;30;47m8[0;5;33;40m%[0;5;35;40mt[0;1;30;43m8[0;5;35;41m@[0;5;33;40mX[0;1;30;41m8[0;1;30;43m8[0;5;33;41mS[0;5;33;40m:[0;1;30;43m8[0;1;30;41m8[0;5;31;40m8[0;1;30;41m8[0;32;40m@[0;5;30;40m8[0;1;30;40m88888888888888[0m'
    print '[0;5;30;40m8[0;5;34;40m8[0;1;30;40m8[0;5;34;40m8[0;1;30;40m8[0;5;34;40m@[0;1;30;40m8[0;5;34;40m8[0;1;30;40m8[0;5;34;40m@[0;1;30;40m8[0;5;34;40m@[0;1;30;40m8[0;5;34;40m8[0;1;30;40m8[0;5;34;40m8[0;1;30;40m8[0;5;34;40m@[0;1;30;40m8[0;5;34;40m8[0;1;30;40m8[0;5;34;40m@[0;1;30;40m8[0;5;34;40m8[0;1;30;40m8[0;5;34;40m@[0;1;30;40m8[0;5;34;40m8[0;1;30;40m88[0;5;35;40m%[0;1;30;43m8[0;5;37;41m8[0;33;47m@[0;37;43m8[0;1;31;45m8[0;33;47m8[0;1;30;47m8[0;1;30;43m88[0;35;41m8[0;5;33;40m8[0;1;30;41m8[0;5;33;40m8[0;5;31;40mX[0;5;30;40m8[0;5;34;40m8[0;1;30;40m8[0;5;34;40m8[0;1;30;40m8[0;5;34;40m8[0;1;30;40m8[0;5;34;40m@[0;1;30;40m8[0;5;34;40m8[0;1;30;40m8[0;5;34;40m@[0;1;30;40m8[0;5;34;40m@[0;1;30;40m8[0m'
    print '[0;5;34;40m8[0;1;30;40m8[0;5;30;40mSX[0;5;34;40m@[0;32;40m8[0;5;34;40m@[0;5;30;40m8X@[0;5;34;40m@[0;32;40m8[0;5;34;40m@[0;5;30;40m8XX[0;5;34;40m@[0;32;40m8[0;5;34;40m@[0;5;30;40m8X@[0;5;34;40m@[0;32;40m8[0;5;34;40m@[0;1;30;40m8[0;5;34;40mS[0;1;30;40m8[0;5;34;40mS[0;5;30;40m@[0;5;35;40m%[0;1;30;43m8[0;5;35;40m.[0;5;33;41m;[0;1;30;47m8[0;1;30;43m8[0;1;31;47m8[0;1;31;43m8[0;1;30;47m8[0;5;31;41m@[0;5;33;40mS[0;5;31;40m88[0;5;33;40m8[0;1;30;41m8[0;1;30;40m8[0;5;34;40m@[0;1;30;40m8[0;5;30;40mSX@[0;5;34;40m@[0;32;40m8[0;5;34;40m@[0;5;30;40m8X@[0;5;34;40m@[0;32;40m8[0;5;34;40m@[0m'
    print '[0;5;34;40mXSX[0;1;30;40m8[0;5;36;40m8[0;5;34;40m8[0;5;30;40mX[0;5;34;40mS[0;1;30;44m8[0;5;32;40mX[0;1;30;44m8[0;5;34;40mS[0;5;30;40mS[0;5;34;40mS[0;1;30;44m8[0;1;30;42m8[0;1;30;44m8[0;5;34;40mX[0;5;30;40mS[0;5;34;40mS[0;1;30;44m8[0;5;32;40mX[0;1;30;44m8[0;5;34;40mS[0;5;30;40mS[0;5;36;40m8[0;1;30;40m8[0;5;36;40m8[0;34;40m8[0;5;36;40m8[0;5;31;40m8[0;5;33;40m% [0;1;30;47m8[0;5;33;41mX[0;1;30;47m8[0;1;31;43m8[0;5;33;40m [0;5;33;41mX[0;5;33;40m;[0;31;43m8[0;5;31;40m@[0;5;33;40m8[0;31;40m@[0;34;40mt[0;32;40m%[0;1;30;40m8[0;5;30;40m@[0;1;30;44m8[0;5;32;40mS[0;30;44m8[0;5;36;40m8[0;5;34;40m8[0;5;30;40mX[0;5;34;40mS[0;1;30;44m8[0;5;32;40mX[0;1;30;44m8[0;5;34;40mS[0;5;30;40mS[0m'
    print '[0;5;36;40m8[0;5;34;40m8[0;5;36;40m8[0;5;34;40m8[0;5;30;40m@[0;5;34;40mS[0;5;36;40m8[0;5;34;40m@[0;5;32;40mS[0;1;30;44m8[0;5;32;40mS[0;1;30;44m8[0;5;36;40m8[0;5;30;40m@[0;5;36;40m8[0;1;30;44m@[0;5;32;40mS[0;5;34;40m@[0;5;36;40m8[0;1;30;40m8[0;5;36;40m8[0;1;30;44m8[0;5;32;40mX[0;1;30;44m8[0;32;40mX[0;34;40m8[0;1;30;40m8X[0;32;40mS[0;31;40m%[0;1;30;40m8[0;1;30;43m8[0;5;35;41m8[0;5;33;40mS%[0;31;43m8[0;1;30;47m8[0;5;33;41m8[0;5;33;40m:[0;1;30;41m8[0;5;31;40m8[0;5;33;40m.[0;5;31;40m@[0;1;30;40mS[0;31;40mt[0;1;30;40mXX[0;32;40mS[0;1;30;40mS[0;32;40m%[0;1;30;40m8@@[0;5;30;40m@S[0;5;36;40m8[0;30;44m8[0;5;36;40m8[0;5;34;40mX[0;5;36;40m8[0m'
    print '[0;5;36;40m@[0;5;34;40m@S[0;5;36;40m8[0;5;34;40mX[0;5;36;40m8[0;1;30;44m8[0;5;36;40m8[0;1;30;44m8[0;5;36;40m8[0;5;34;40m@[0;5;36;40m8[0;1;30;44m8[0;5;36;40m8[0;5;34;40m8[0;5;36;40m8[0;5;34;40m8S[0;5;36;40m8[0;1;30;44m8[0;5;36;40m8[0;5;34;40m@[0;5;30;40m@[0;32;40m%[0;5;30;40m8[0;1;30;40m8@XXS[0;31;40mS[0;5;35;40mt[0;1;30;43m8[0;35;47m8[0;5;33;41mS[0;1;30;47m8[0;1;31;41m8[0;5;33;40mt[0;33;41m8[0;5;33;40mt[0;1;30;47m8t[0;31;40m@[0;1;30;40m88[0;32;40m;[0;1;30;40m@8@8@@X[0;32;40mS[0;34;40mS[0;32;40m%[0;5;30;40m8[0;5;34;40mX[0;5;36;40m8[0;5;34;40m8[0m'
    print '[0;5;36;40m@8[0;5;34;40m8[0;5;36;40m8[0;5;34;40m8[0;5;36;40m8[0;5;34;40m@[0;5;36;40m88[0;5;34;40m8[0;5;36;40m8[0;5;34;40m@[0;5;36;40m8[0;5;34;40m8[0;5;36;40m8[0;5;34;40m8[0;5;36;40m88[0;5;34;40m8[0;5;36;40m8[0;5;34;40m8[0;5;36;40m8[0;34;40m8[0;1;30;40m8XXX[0;31;40m%[0;1;30;40mX[0;34;40mt[0;31;40m%[0;1;30;40mX[0;1;30;41mX[0;5;33;40m8 [0;31;43m8[0;5;33;40m%:[0;1;30;47m8S[0;1;37;47m [0;1;30;47m8[0;31;40mS[0;1;30;40m8@S[0;31;40mt[0;1;30;40m8X@888@[0;31;40m%[0;1;30;40mX[0;32;40m;[0;1;30;40mS[0;5;36;40m8[0;5;34;40m8[0m'
    print '[0;5;36;40mX@@88@8[0;5;34;40m@[0;5;36;40m@@@@@@@X[0;5;34;40m@[0;5;36;40m8@X@[0;5;34;40m@[0;1;30;40mXXXXX@[0;32;40mt[0;1;30;40mX[0;32;40mt[0;34;40m%[0;31;40m;[0;5;31;40mX[0;1;30;47m;[0;5;35;40mtS[0;5;33;40mX[0;5;35;40m:[0;1;37;47m  [0;5;33;40mX[0;1;30;40mX@@SXX8888[0;31;40mS[0;1;30;40m@[0;32;40mt[0;34;40m%[0;31;40m%[0;1;30;40m8[0;5;36;40m@X[0m'
    print '[0;5;36;40mS[0;1;30;46m8[0;1;30;45m8[0;1;30;46m8[0;5;36;44m8[0;5;35;40m.[0;1;30;46m88[0;1;30;45m8[0;1;30;46m8[0;1;34;46m8[0;5;35;40m:[0;1;30;46m8[0;1;30;45m8[0;1;34;46m8[0;5;36;40m:[0;1;30;46m8[0;5;36;40m;[0;5;36;44m@[0;5;36;40m @[0;34;40m@[0;31;40mt[0;1;30;40mX[0;32;40mt[0;1;30;40m@X[0;34;40mt[0;1;30;40mX[0;31;40mt[0;1;30;40m@S[0;34;40m;[0;5;30;40m8[0;1;30;47m8[0;5;35;40m;[0;5;33;40mX[0;5;35;40mt[0;1;30;47mt[0;1;37;47m  [0;5;31;40m8[0;34;40mt[0;1;30;40m8X[0;32;40m;[0;1;30;40mXXX[0;31;40m%[0;1;30;40m8X[0;32;40mS[0;1;30;40mX[0;34;40mt[0;1;30;40m@[0;32;40mt[0;5;34;40m8[0;5;36;40mS[0;1;30;46m8[0m'
    print '[0;5;36;40m%[0;1;30;46m8[0;5;36;44mt[0;1;30;47m8[0;1;30;46m8[0;36;47m8[0;5;35;44mX[0;36;47m8[0;1;34;46m8[0;1;30;47m8[0;1;30;46m8[0;5;37;44m8[0;1;30;46m8[0;37;46m8[0;5;36;40m.[0;5;36;44m;[0;1;30;47m8[0;1;34;46m8[0;1;30;47m8[0;1;30;46m8[0;5;35;40mt[0;5;31;40m8[0;32;40mt[0;34;40m%[0;1;30;40mX[0;31;40mt[0;1;30;40m@[0;32;40mt[0;1;30;40mX[0;34;40m%[0;1;30;40mX[0;32;40mt[0;34;40mt[0;5;30;40m8[0;5;35;40m [0;5;33;40mt[0;5;35;40mX[0;5;33;40m%[0;1;37;47m :%[0;31;40mX[0;1;30;40m@[0;32;40m%[0;1;30;40m@X[0;31;40m%[0;1;30;40mX[0;32;40mt[0;1;30;40m@SS[0;34;40m%[0;31;40m%[0;1;30;40m@X[0;31;40m%[0;5;36;40m8%[0;1;30;46m8[0m'
    print '[0;1;30;46m8[0;1;30;47m8[0;37;46m8[0;1;34;46m8[0;1;30;47m8[0;1;34;46m8[0;1;30;47m8[0;1;30;46m8[0;36;47m8[0;5;36;44mS[0;1;30;47m8[0;1;30;46m8[0;1;34;47m8[0;1;34;46m8[0;1;30;47m8[0;37;46m88[0;1;30;46m8[0;5;37;44m8[0;5;34;40mS[0;5;33;40m [0;1;30;43m8[0;31;40m8[0;34;40m%[0;32;40m%[0;34;40m%[0;1;30;40mX[0;31;40mt[0;1;30;40mX[0;32;40m%[0;1;30;40m@[0;31;40m%[0;1;30;40mS[0;5;31;40mX[0;5;35;40m .[0;5;33;40m.:[0;1;37;47m % [0;31;40mX[0;1;30;40m@[0;5;30;40m8[0;31;40m8[0;1;30;40m8[0;34;40mt[0;32;40mt[0;1;30;40m@[0;34;40mt[0;31;40mt[0;32;40m%[0;31;40m%[0;1;30;40m8[0;32;40m%[0;1;30;40m@[0;34;40m;[0;1;30;40m8[0;5;36;40mS[0;5;36;44mX[0m'
    print '[0;1;30;46m8[0;36;47m8[0;5;36;44m%[0;1;30;47mX[0;1;34;46m8[0;1;30;47m8[0;1;34;46m8[0;36;47m8[0;5;37;44m8[0;36;47m8[0;1;34;46m8[0;36;47m@88[0;5;36;44m;[0;36;47m8[0;5;36;44m%[0;1;30;47m8[0;5;37;40mX[0;5;33;40m:[0;5;33;41m%[0;5;33;40m ;[0;1;30;43m8[0;1;30;47m8[0;31;40m8[0;32;40mt[0;34;40m%[0;1;30;40mX[0;31;40m%[0;34;40mS[0;1;30;40mX[0;32;40m;[0;5;35;40m [0;5;37;40mtt:[0;1;30;43m8[0;1;37;47m.;[0;33;47m8[0;31;40mX[0;1;30;40m@XX[0;32;40mt[0;31;40m;[0;34;40m%[0;31;40m%[0;32;40mS[0;34;40m%[0;1;30;40mS[0;32;40mt[0;1;30;40mX@[0;31;40mt[0;1;30;40m@[0;34;40mX[0;5;30;40mX[0;1;30;47m8[0m'
    print '[0;1;30;46m8[0;36;47m888[0;1;34;47m8[0;37;46m@[0;1;34;47m8[0;37;46m88[0;1;34;47m8[0;36;47m8[0;5;36;44m;[0;36;47m8888[0;5;36;40m;[0;5;34;40mS[0;37;43m8[0;33;47m8[0;1;30;47m8[0;1;31;43m8[0;5;37;40mt[0;1;30;43m8[0;5;33;41m8[0;1;30;47m8[0;5;33;40m8[0;1;30;41m@[0;32;40m;[0;1;30;40mXS[0;34;40m;[0;1;30;40m@[0;5;33;40m [0;1;30;47m8[0;5;33;40m;[0;35;47m8[0;37;43m8[0;1;37;47m ;[0;1;30;47m8[0;31;40m@[0;1;30;40mX[0;32;40mt[0;34;40m%[0;1;30;40mS[0;32;40m;[0;1;30;40mS[0;34;40mt[0;31;40m%[0;32;40mt[0;31;40mt[0;34;40mX[0;1;30;40mX[0;31;40mt[0;1;30;40m8X[0;31;40m%[0;34;40mS[0;1;30;46m8[0m'
    print '[0;37;46m8[0;5;37;44m8[0;37;46m8[0;5;36;44m [0;36;47m88[0;5;36;44m [0;36;47m@[0;5;37;44m8[0;37;46m@[0;36;47m88[0;5;36;44m [0;36;47m8[0;5;36;44mX[0;5;34;40m@[0;34;40mS[0;5;31;40m8[0;1;30;43m8[0;5;37;41m8[0;1;30;43m8[0;1;30;47m8[0;5;37;41m8[0;33;47m8[0;1;30;43m8[0;5;33;41mS[0;5;33;40m [0;5;31;40mX[0;32;40m;[0;34;40mt[0;1;30;40mX[0;31;40mt[0;5;30;40m8[0;5;33;40m;;.[0;5;33;41m8[0;5;35;40m;[0;1;37;47m:t[0;33;47m8[0;31;40mS[0;1;30;40mXX[0;31;40mt[0;34;40m;[0;31;40mt[0;32;40mt[0;1;30;40mX[0;34;40m;[0;31;40mt[0;1;30;40m8@88X@@8[0;5;36;40mX[0m'
greeting()

if u.url[0]==" ":
    ur=raw_input("Ugur Dundar expects an url without http://\n-->")
    url='http://'+ur
else:
    url='http://'+u.url[0]
print "Url you provided to Ugur Dundar is %s"%url

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class ugur():
    def get(self):
        self.durum=True
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
        elif usr_sel=='d':
            self.durum=False
        else:
            print "Wrong key use s for see inside or r for remove or d for done...\nNow try again"
            return ugur.whattodo(self,tagname)  
    def first_time(self,soup,tagname):
        self.check_1=[]
        for tag in soup.find_all(tagname):
            self.check_1.append(tag.get_text())
            print bcolors.HEADER+tag.get_text()+bcolors.ENDC
    def check2(self,tagname):
        ugur.get(self)
        self.check_2=[]
        for tag in self.soup.find_all(tagname):
            self.check_2.append(tag.get_text())
    def crosscheck(self):
        if self.check_1!=self.check_2:
            tmp=set(self.check_1) ^ set(self.check_2)
            print bcolors.OKGREEN+tmp.pop()+bcolors.ENDC
            self.check_1=self.check_2
        else:
            print bcolors.WARNING+"no change"+bcolors.ENDC
        
if __name__=='__main__':
    x=ugur()
    x.get()
    clr=raw_input("Do you want Ugur Dundar to clear scripts for you ?? (y/n):")
    if clr=='y':
        x.removetags(x.soup, "script")
    else:
        pass
    print x.soup.prettify()
    while(x.durum==True):
        x.printtags(x.soup)
        tagname=x.selectagname()
        x.whattodo(tagname)
        
    x.first_time(x.soup, tagname)
    interval=int(raw_input("Gimme time interval for your searchs in secs:"))
    while(True):
        x.check2(tagname)
        x.crosscheck()
        sleep(interval)
        

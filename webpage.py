from bs4 import BeautifulSoup
import requests
from time import sleep

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get():
    r = requests.get("http://ikc.edu.tr/Duyuru")
    data=r.text
    soup=BeautifulSoup(data,'html.parser')
    return soup

def firsttime(soup):
    for i in soup.find_all("p"):
        if i.find_all('em')!=[]:
            a=str(i.find_all('em'))
            new_a=a.split('>')[1]
            a=new_a.split('<')[0]
            print bcolors.HEADER+a.decode('unicode_escape')+bcolors.ENDC

def check1(soup):
    result1=[]
    for i in soup.find_all('p'):       
        result1.append(i.find_all('em'))
    return result1

def check2(soup):
    result2=[]
    for i in soup.find_all('p'):
        result2.append(i.find_all('em'))
    return result2

def crosscheck(result1,result2):
    if result1[0]!=result2[0]:
        print bcolors.OKGREEN+result2[0]+bcolors.ENDC
        get()
        check1(soup)
        check2(soup)
    else:
        print bcolors.WARNING+"no change"+bcolors.ENDC
        
def hourlywork():
    get()
    check2(soup)
    crosscheck(result1, result2)
    
soup=get()
firsttime(soup)
result1=check1(soup)
result2=check2(soup)
while(True):
    hourlywork()
    sleep(1800)
    

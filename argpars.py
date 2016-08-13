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
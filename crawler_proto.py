# To run this, download the BeautifulSoup and install
# http://www.py4e.com/code3/bs4.zip

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
##
import socket

mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##


# Ignore SSL certificate errors: i dont know in detail but use this piece of code
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#some uarl u r starting with. comment this if you are prompting url using input
url = 'http://py4e-data.dr-chuck.net/'

#C:\Users\DmM67\AppData\Roaming\Python\Python38\Scripts
#C:\Users\DmM67\AppData\Roaming\Python\Python38\Scripts' which is not on PATH.
fh = open("py_write.txt",'w')

#counter variable that is used to limit loop
lim=0;

#list to store URL's
ulist = list()

##
print(url)
mysock.connect(('www.dr-chuck.com',80))
cmd='GET http://www.dr-chuck.com/page2.htm HTTP/1.0 \n\n'.encode()
print(cmd)
mysock.send(cmd)
while True:
    data=mysock.recv(512)
    if(len(data)<1):
        break
    print(data.decode())
    fh.write(data.decode())
mysock.close()

##
 #either use code  between "##" and "##" or uncomment following incomplete code

###def crawling(url,lim) :
    ###while True:

        ###lim=lim+1

        ###if lim >30 :
            ###break

            #url = input('Enter - ')

        ##html = urllib.request.urlopen(url, context=ctx).read()
        ##soup = BeautifulSoup(html, 'html.parser')

        # Retrieve all of the anchor tags
        ##tags = soup('a')
        ##for tag in tags:
            ##u=tag.get('href', None)
            ##ulist.append(u[:5])
            ##print(len(ulist))
            #print(ulist)
            ##for content in ulist :
                ##fh.write(content)

            ##klim=0
            ##for item in ulist :
                ##klim=klim+1
                ##url = item;
                ##crawling(url,lim)
                ##if klim > 5 or lim >30 :
                    ##break


        ###print(ulist)
###crawling(url,lim)

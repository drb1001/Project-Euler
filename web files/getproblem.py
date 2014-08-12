import urllib
from bs4 import BeautifulSoup
import os


# specify problem number
var = raw_input("Problem number: ")
myurl = "https://projecteuler.net/problem=" + var


# retrieve html
print myurl
print "Retrieving html ... "
sock = urllib.urlopen(myurl)
htmlSource = sock.read()
sock.close()


# extract and format text
soup = BeautifulSoup(htmlSource)

mytitle = soup.html.head.title.get_text()

mycontent = soup.find("div", {"class": "problem_content"})
mycontent = mycontent.findAll(text=True)
mycontent = [x.replace('\n', '\n#  ') for x in mycontent]
mycontent = "".join(mycontent)

myoutput = "\n###\n#  " + mytitle \
           + "\n#  " + myurl \
           + "\n#  " \
           + "\n#  " + mycontent \
           + "\n###\n\n"

print myoutput


# check if file exists
filename = "problem" + var + ".py"
myrootdir = '..'

for root, dirs, files in os.walk(myrootdir):
    for allfiles in files:
        if allfiles == filename:
            myfilepath = root + "/" + allfiles


# if file exists add as comment
print myfilepath
with file(myfilepath, 'r') as original:
    data = original.read()
    with file(myfilepath, 'w') as modified: modified.write(myoutput + data)

# if file does not exist - create file and add comment

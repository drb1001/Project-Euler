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
soup = BeautifulSoup(htmlSource, "html.parser")

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

# really crappy way to replace all unicode chars
myoutput = myoutput.replace (u'\xd7', "x")   # replace unicode multiply sign
myoutput = myoutput.replace (u'\u2212', "-")   # replace unicode minus sign
myoutput = myoutput.replace (u'\u2260', "!=")   # replace unicode not equal sign
myoutput = myoutput.replace (u'\xa0', " ")   # replace unicode no-break space
myoutput = myoutput.replace (u'\xb2', "^2")   # replace unicode squared
myoutput = myoutput.replace (u'\u2264', "<=")   # replace unicode less than equal to


print myoutput

# check if file exists
filename = "problem" + var + ".py"
myrootdir = '..'

for root, dirs, files in os.walk(myrootdir):
    for allfiles in files:
        if allfiles == filename:
            myfilepath = root + "/" + allfiles


# if file exists add as comment
print "writing to:  " +  myfilepath
with file(myfilepath, 'r+') as myfile:
    old_data = myfile.read()
    myfile.seek(0)
    try:
        myfile.write(myoutput + old_data)
    except Exception as e:
        print "Error in writing new data: " + str(e)
        myfile.write(old_data)

# if file does not exist - create file and add comment

import urllib
import bs4

var = "2" #raw_input("Problem number: ")
print var
myurl = "https://projecteuler.net/problem=" + var



sock = urllib.urlopen(myurl)
htmlSource = sock.read()
sock.close()

print (htmlSource)


file = open('myfile.dat', 'w+')

# extract data
# check if file exists
# if file exists add as comment
# if file does not exist - create file and add comment

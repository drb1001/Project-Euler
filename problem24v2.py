# Project Euler
# problem 24

import itertools

mylist = list(itertools.permutations( range(0,10) ))
mynumber = (mylist[999999])
print str(mynumber)

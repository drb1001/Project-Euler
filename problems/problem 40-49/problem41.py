# Project Euler
# problem 41

import itertools,math

def isprime(n):
    if n%10 in (0,2,4,5,6,8):
        return False
    for i in range(2,int(math.sqrt(n))):
        if float(n)/i %1 == 0:
            return False
    return True

mylist = list(itertools.permutations( range(0,10) ))
mylist.reverse()
print len(mylist)

counter=0

for number in mylist:
    counter=+1
    mynumber = int( ''.join( map(str,list(number)) ) )
    if isprime(mynumber):
        print mynumber
        break
    if counter%10000==0: print counter

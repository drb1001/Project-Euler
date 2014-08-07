# Project Euler
# Problem 4

import math

def ispal(n):
    s=str(n)
    l=len(s)
    if l==1 or l==0:
        return True
    if l==2 and s[0]==s[-1]:
        return True
    elif s[0]==s[-1]:
        return ispal(s[1:-1])
    else:
        return False


largest=0
fact=[0,0]
for i in range(999,100,-1):
    for j in range(i,100,-1):
        prod=i*j
        if ispal(prod):
            if largest<prod:
                largest=prod
                factors=[i,j]
print "Largest = " + str(largest) + " , " + str(factors)

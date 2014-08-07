# Euler challenge
# Problem 12

from math import sqrt

def trianglenum(n):
    return ((n*(n+1))//2)

def boolprimesupto(n):
    boolprimes = [True for i in range(0,n+1)]
    boolprimes[0]=False
    boolprimes[1]=False
    for index in range(0,int(sqrt(n))+1):
        if boolprimes[index]:
            for multiples in range(index*index,n+1,index):
                boolprimes[multiples]=False
    return boolprimes

boolprimesupto100000=boolprimesupto(100000)


def numberofdiv(n):
    totalcount=1
    for prime in range(0,int(sqrt(n))):
        keepgoing=True
        indexcount=1
        if boolprimesupto100000[prime]:
            while keepgoing:
                if (n/float(prime))%1==0:
                    n=n/prime
                    indexcount=indexcount+1
                    keepgoing=True
                else:
                    keepgoing=False
            totalcount=totalcount*indexcount
    return totalcount

maxnod=0
for n in range(2,100000):
    trin=trianglenum(n)
    nod=numberofdiv(trin)
    if maxnod<nod:
        maxnod=nod
    if n%50==0:
        print n,trin,nod, maxnod
    if nod>500:
        print n,trin,nod
        break


##def numberofdiv2(n):
##    if n==1:
##        return 1
##    count=2
##    for i in range(2,sqrt(n)):
##        trial=n/float(i)
##        if trial%1==0:
##            newn=int(trial)
##            count=count+numberofdiv(newn)
##            break
##    return count*2
##
##def numberofdiv3(n):
##    count=2
##    for i in range(2,n):
##        trial=n/float(i)
##        if trial%1==0:
##            newn=int(trial)
##            count=count+1
##    return count

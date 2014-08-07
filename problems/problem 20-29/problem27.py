# project euler
# problem 27
from math import sqrt

def boolprimesupto(n):
    boolprimes = [True for i in range(0,n+1)]
    boolprimes[0]=False
    boolprimes[1]=False
    for index in range(0,int(sqrt(n))+1):
        if boolprimes[index]:
            for multiples in range(index*index,n+1,index):
                boolprimes[multiples]=False
    return boolprimes

boolprimesupto2mil=boolprimesupto(2000000)
print boolprimesupto2mil[:10]
print "-----"

primesupto1k=[]
for i in range(0,1001):
    if boolprimesupto2mil[i]:
        primesupto1k.append(i)

print len(primesupto1k)
print primesupto1k[:10]
print "-----"

maxprimecount=[0,0,0]
for a in range(-1000,1001):
    for b in primesupto1k:
        primecount=0
        for n in range(0,1000):
            eq = n*n + a*n + b
            if eq>0:
                if boolprimesupto2mil[eq]==True:
                    primecount+=1
                else:
                    break
            else:
                break
        if maxprimecount[2]<primecount:
            maxprimecount=[a,b,primecount]
            print maxprimecount

print maxprimecount, maxprimecount[0]*maxprimecount[1]

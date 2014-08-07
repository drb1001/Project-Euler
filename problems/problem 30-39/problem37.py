# project euler
# problem 35
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

boolprimesupto1mil=boolprimesupto(1000000)
print boolprimesupto1mil[:10]
print "-----"

mycount=0
mysum=0
for n in range(10,1000000):
    if boolprimesupto1mil[n]==False:
        continue   
    sn=str(n)
    l=len(sn)
    for i in range(1,l):
        newn1=int(sn[:l-i])
        if boolprimesupto1mil[newn1]==False:
            break
        newn2=int(sn[l-i:])
        if boolprimesupto1mil[newn2]==False:
            break
    else:
        mysum=mysum+n
        mycount+=1
        print mycount,n,mysum
        if mycount==11:
            break

print "________"
print mycount,mysum

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
for n in range(1,1000000):
    sn=str(n)
    l=len(sn)
    if boolprimesupto1mil[n]==False:
        continue
    if l==1:
        mycount+=1
        print n,l
    if l>1:
        for i in range(1,l):  
            newn=int(sn[l-i:]+sn[:l-i])
            if str(newn)[l-1] in [0,2,4,5,6,8]:
                break
            if boolprimesupto1mil[newn]==False:
                break
            if i==l-1:
                mycount+=1
                print n,l,newn,i

print "________"
print mycount

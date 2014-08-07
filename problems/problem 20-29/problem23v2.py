# Project Euler
# problem 23

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

boolprimesupto30k=boolprimesupto(30000)


def sumofpropdiv(n):
    if n==1 or boolprimesupto30k[n]:
        return 1
    output=1
    checkupto=n
    for test in range(2,n):
        if test >= checkupto:
            break
        testdiv = n/float(test)
        if (testdiv)%1==0:
            output+=test
            if testdiv!=test:
                output+=testdiv
        checkupto = min(checkupto,int(testdiv))
    return output

# 0=perf, 1=abund, -1=def
binabundnum = [ 0 for i in range(0,30000) ]

for n in range(1,30000):
    if n%1000==0:
        print n
    dn=sumofpropdiv(n)
    if n==dn:
        binabundnum[n]=0
    elif n<dn:
        binabundnum[n]=1
    else:
        binabundnum[n]=-1

print "---------"
print binabundnum[:20]
print "---------"


abundnum=[]
for n in range(1,30000):
    if binabundnum[n] == 1:
        abundnum.append(n)

print "---------"
print abundnum[:20]
print "---------"

runningtotal=0
for test in range(1,30000):
    if test%1000==0:
        print test
    for abund in abundnum:
        if abund >= test:
            runningtotal = runningtotal + test
            #print test, abund
            break
        elif binabundnum[(test-abund)]==1:
            #print test, abund, test-abund
            break

print "---------"
print runningtotal

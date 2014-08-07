# project euler
# problem 46
from math import sqrt
from time import clock

start=clock()

def boolprimesupto(n):
    boolprimes = [True for i in range(0,n+1)]
    boolprimes[0]=False
    boolprimes[1]=False
    for index in range(0,int(sqrt(n))+1):
        if boolprimes[index]:
            for multiples in range(index*index,n+1,index):
                boolprimes[multiples]=False
    return boolprimes

isprime=boolprimesupto(100000)


exit=False
for n in range(3,100000,2):
    if isprime[n]:
        continue
    if exit:
        break
    for i in range( 1,int(sqrt(n)) ):
        test = n - 2*i*i
        if test<0:
            print n
            exit=True
            break
        elif isprime[test]:
            #print "%d = %d + 2x(%d^2) = %d + %d" %(n,test,i,test,(2*i*i))
            break

print "Time: " + str(clock()-start)


###
#  Problem 27 - Project Euler
#  https://projecteuler.net/problem=27
#
#
#  Euler discovered the remarkable quadratic formula:
#  n^2 + n + 41
#  It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
#  The incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.
#  Considering quadratics of the form:
#
#  n^2 + an + b, where |a| < 1000 and |b| < 1000where |n| is the modulus/absolute value of ne.g. |11| = 11 and |-4| = 4
#
#  Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
#
###

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

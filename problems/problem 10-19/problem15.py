# Project Euler
# problem 15

from math import factorial

def choose(n,k):
    t=factorial(n)/(factorial(n-k)*factorial(k))
    return t

mysum=0
for i in range(1,21):
    ichoose20=choose(20,i)
    print ichoose20
    mysum = mysum + ichoose20*ichoose20

print mysum

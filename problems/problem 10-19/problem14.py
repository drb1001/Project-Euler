# Project Euler
# Problem 14

def myfunc(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

def seqlen(n):
    if n<=0:
        return 0
    counter=1
    while n!=1:
        n=myfunc(n)
        counter+=1
    return counter

maxchain=0
for n in range(0,1000000):
    newlen=seqlen(n)
    if maxchain < newlen:
        maxchain = newlen
        print n, maxchain

print maxchain

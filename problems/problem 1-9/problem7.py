# Project Euler
# Problem 7

def primesupto(n):
    primes=[2,3,5]
    for i in range(7,n+1,2):
        isprime=True
        for prime in primes:
            if i%prime==0:
                isprime=False
                break
        if isprime:
            primes.append(i)
    return primes

primesupto120000=primesupto(120000)
print len(primesupto120000)
print primesupto120000[10000]

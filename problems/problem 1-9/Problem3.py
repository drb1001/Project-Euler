# Project Euler
# Problem 3

import math

sroot = int(math.sqrt(600851475143))


def primesupto(n):
    primes=[2,3,5]
    for i in range(6,n+1):
        isprime=True
        for prime in primes:
            if i%prime==0:
                isprime=False
                break
        if isprime:
            primes.append(i)
    return primes


#print primesupto(sroot)[-1]

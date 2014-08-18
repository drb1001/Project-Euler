#####
# functions for getting lists of prime numbers
#####

from math import sqrt


# slow / naive method of creating an array of primes
# array contains all primes upto input n
def listprimesupto(n):
    primes = [2,3,5]
    for i in range(6, n+1):
        isprime = True
        for prime in primes:
            if i % prime == 0:
                isprime = False
                break
        if isprime:
            primes.append(i)
    return primes


# faster way of listing primes, using sieve
# boolean array contains all numbers, true = prime
def boolprimesupto(n):
    boolprimes = [True for i in range(0, n+1)]
    boolprimes[0] = False
    boolprimes[1] = False
    for index in range(0, int(sqrt(n))+1):
        if boolprimes[index]:
            for multiples in range(index * index, n+1, index):
                boolprimes[multiples] = False
    return boolprimes
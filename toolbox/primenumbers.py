#####
# functions for getting lists of prime numbers
#####

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

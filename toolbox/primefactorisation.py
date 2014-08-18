#####
# functions for prime factorisation of a number
#####

import math
from toolbox import primenumbers


# return array of prime factors
# repeated prime factors will be in the array multiple times
def primefactors(n):

    sqrtn = int(math.sqrt(n))
    primes = primenumbers.listprimesupto(sqrtn)

    nnew = n
    factors = []

    for p in primes:
        if p > nnew: break

        while nnew % p == 0:
            if nnew == p: break
            factors.append(p)
            nnew = nnew / p

    factors.append(nnew)
    return factors



# return array of array of prime factors
# repeated prime factors will be in array once, with associated count
def primefactorsarray(n):
    factorslist = primefactors(n)
    factors = [[factorslist[0], 0]]
    for new in factorslist:
        found = False
        for f in factors:
            if f[0] == new:
                f[1] = f[1] + 1
                found = True
                break
        if found == False:
            factors.append([new, 1])
    return factors


# testing
# print primefactors(2560)
# print primefactorsarray(2560)
#
# print primefactors(81)
# print primefactorsarray(81)
#
# print primefactors(5)
# print primefactorsarray(5)
#
# print primefactors(29160)
# print primefactorsarray(29160)
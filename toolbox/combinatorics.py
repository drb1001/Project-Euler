#####
# functions for combinatorics
#####

from math import factorial


def choose(n,k):
    t = factorial(n) / (factorial(n-k) * factorial(k))
    return t

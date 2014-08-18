###
#  Problem 6 - Project Euler
#  https://projecteuler.net/problem=6
#
#
#  The sum of the squares of the first ten natural numbers is,
#  12 + 22 + ... + 102 = 385
#  The square of the sum of the first ten natural numbers is,
#  (1 + 2 + ... + 10)**2 = 55**2 = 3025
#  Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#  Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#
###


# Project Euler
# Problem 6

def sumof1to(n):
    return (n * (n + 1)) // 2

def sumofsq1to(n):
    return (n * (n + 1) * ((2 * n) + 1)) // 6


print sumof1to(100) * sumof1to(100)
print sumofsq1to(100)
print (sumof1to(100) * sumof1to(100)) - sumofsq1to(100)

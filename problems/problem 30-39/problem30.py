
###
#  Problem 30 - Project Euler
#  https://projecteuler.net/problem=30
#
#
#  Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#  1634 = 14 + 64 + 34 + 44
#  8208 = 84 + 24 + 04 + 84
#  9474 = 94 + 44 + 74 + 44
#  As 1 = 14 is not a sum it is not included.
#  The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#  Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
#
###

# project euler
# problem 30

from math import pow

runningsum=0
for i in range(10,1000000):
    s=str(i)
    total=0
    for n in s:
        x=int(n)
        x5=int(pow(x,5))
        total=total+x5
    if i==total:
        print i, total
        runningsum=runningsum+i


print "-----------"
print runningsum

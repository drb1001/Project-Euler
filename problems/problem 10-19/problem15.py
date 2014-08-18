
###
#  Problem 15 - Project Euler
#  https://projecteuler.net/problem=15
#  
#  
#  Starting in the top left corner of a 22 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#  
#  
#  
#  How many such routes are there through a 2020 grid?
#  
###

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

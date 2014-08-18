
###
#  Problem 15 - Project Euler
#  https://projecteuler.net/problem=15
#  
#  
#  Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#  
#  How many such routes are there through a 2020 grid?
#  
###

# Project Euler
# problem 15

from toolbox import combinatorics

mysum = 0
for i in range(1,21):
    ichoose20 = combinatorics.choose(20,i)
    mysum = mysum + ichoose20 * ichoose20

print mysum


###
#  Problem 5 - Project Euler
#  https://projecteuler.net/problem=5
#  
#  
#  2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#  What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#  
###

# Project Euler
# Problem 5


out = 2520*11*13*17*19*2
print out

for i in range(1,20):
    print i, out/float(i)

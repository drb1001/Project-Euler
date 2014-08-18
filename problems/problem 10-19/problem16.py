
###
#  Problem 16 - Project Euler
#  https://projecteuler.net/problem=16
#  
#  
#  2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#  What is the sum of the digits of the number 2^1000?
#  
###

# Project Euler
# problem 16

from toolbox import numberproperties

total = 1
for i in range(0,100):
    total = total * 1024

print numberproperties.sumdigits(total)

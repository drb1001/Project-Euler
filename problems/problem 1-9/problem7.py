
###
#  Problem 7 - Project Euler
#  https://projecteuler.net/problem=7
#  
#  
#  By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#  What is the 10 001st prime number?
#  
###

# Project Euler
# Problem 7


from toolbox import primenumbers

primesupto150000 = primenumbers.listprimesupto(150000)
print primesupto150000[10000]


###
#  Problem 3 - Project Euler
#  https://projecteuler.net/problem=3
#
#
#  The prime factors of 13195 are 5, 7, 13 and 29.
#  What is the largest prime factor of the number 600851475143 ?
#
#  Note: This problem has been changed recently, please check that you are using the right number.
#
#
###

# Project Euler
# Problem 3


from toolbox import primefactorisation

output = primefactorisation.primefactors(600851475143)

print output
print max(output)

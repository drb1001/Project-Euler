
###
#  Problem 10 - Project Euler
#  https://projecteuler.net/problem=10
#  
#
#  The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#  Find the sum of all the primes below two million.
#
#  Note: This problem has been changed recently, please check that you are using the right parameters.
#
#
###

# Project Euler
# Problem 10


from toolbox import primenumbers


boolprimesupto2mil = primenumbers.boolprimesupto(2000000)

total = 0
for n in range(0, len(boolprimesupto2mil)):
    if boolprimesupto2mil[n]:
        total = total + n

print total


###
#  Problem 4 - Project Euler
#  https://projecteuler.net/problem=4
#
#
#  A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.
#  Find the largest palindrome made from the product of two 3-digit numbers.
#
###

# Project Euler
# Problem 4


from toolbox import numberproperties

output = 0
fact = [0,0]
for i in range(999,100,-1):
    for j in range(i,100,-1):
        product = i * j
        if numberproperties.ispal(product):
            if output < product:
                output = product
                factors = [i,j]

print factors
print output

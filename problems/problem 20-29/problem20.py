
###
#  Problem 20 - Project Euler
#  https://projecteuler.net/problem=20
#
#
#  n! means n x (n - 1) x ... x 3 x 2 x 1
#  For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#  Find the sum of the digits in the number 100!
#
###

# Project Euler
# problem 20

def factorial(n):
    output=1
    for i in range(1,n+1):
        output=output*i
    return output

f100=factorial(100)
print f100

strf100=str(f100)
sumtotal=0
for i in strf100:
    sumtotal=sumtotal+int(i)

print sumtotal

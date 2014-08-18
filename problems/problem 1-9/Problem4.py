
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


def ispal(n):
    s = str(n)
    l = len(s)
    if l == 1 or l == 0:
        return True
    elif l == 2 and s[0] == s[-1]:
        return True
    elif s[0] == s[-1]:
        return ispal(s[1:-1])
    else:
        return False


output = 0
fact = [0,0]
for i in range(999,100,-1):
    for j in range(i,100,-1):
        prod = i * j
        if ispal(prod):
            if output < prod:
                output = prod
                factors = [i,j]

print factors
print output

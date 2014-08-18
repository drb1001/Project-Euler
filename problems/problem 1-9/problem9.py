
###
#  Problem 9 - Project Euler
#  https://projecteuler.net/problem=9
#  
#
#  A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
#   a2 + b2 = c2
#  For example, 32 + 42 = 9 + 16 = 25 = 52.
#  There exists exactly one Pythagorean triplet for which a + b + c = 1000.Find the product abc.
#
###

# Project Euler
# Problem 9


# a^2 + b^2 = {1000-(a+b)}^2
#           = 1000000 + (a+b)^2 - 2000(a+b)
#           = 1000000 + a^2 + b^2 +2ab -2000a - 2000b
# 1 000 000 = 2ab - 2000a - 2000b
#   500 000 = a(b - 1000)  - 1000b
# a = (500 000 - 1000b)/(b-1000)
#   = 1000 * [ (500 - b)/(b-1000) ]

from math import sqrt

def sqnumsunder(n):
    output=[]
    for i in range(1,int(sqrt(n))+1):
       output.append(i*i)
    return output


sqnumsunder1000000=sqnumsunder(1000000)
print sqnumsunder1000000

for asq in sqnumsunder1000000:
    for bsq in sqnumsunder1000000:
        for csq in sqnumsunder1000000:
            a=int(sqrt(asq))
            b=int(sqrt(bsq))
            c=int(sqrt(csq))
            if a+b+c==1000:
##                if asq + bsq == csq:
                print a,b,c
##                    print sqrt(asq)*sqrt(bsq)*sqrt(csq)

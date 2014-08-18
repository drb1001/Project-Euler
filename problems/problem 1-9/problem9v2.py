
###
#  Problem 9 - Project Euler
#  https://projecteuler.net/problem=9
#
#
#  A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
#   a2 + b2 = c2
#  For example, 3**2 + 4**2 = 9 + 16 = 25 = 52.
#  There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
#
###


#  Project Euler
# Problem 9


# a^2 + b^2 = {1000-(a+b)}^2
#           = 1000000 + (a+b)^2 - 2000(a+b)
#           = 1000000 + a^2 + b^2 +2ab -2000a - 2000b
#
# 1 000 000 = 2ab - 2000a - 2000b
#   500 000 = a(b - 1000)  - 1000b
#
# a = (500 000 - 1000b)/(b-1000)
#   = 1000 * [ (500 - b)/(b-1000) ]


for b in range(1, 500):
    b = float(b)
    a = 1000 * ((500 - b)/(1000 - b))
    c = 1000 - a - b
    if (a > 0 and a % 1 == 0) and (c > 0 and c % 1 == 0) and (a >= b >= c):
        print int(a), int(b), int(c)
        print int(a * b * c)

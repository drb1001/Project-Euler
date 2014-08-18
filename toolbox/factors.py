#####
# functions for factorisation of a number, finding divisors
#####

from math import sqrt
from toolbox import primefactorisation


# main method to count the number of divisors of a number
def numberofdiv(n):
    totalcount = 1
    pfarray = primefactorisation.primefactorsarray(n)
    for i in pfarray:
        totalcount = totalcount * (i[1] +1)
    return totalcount


# alternative method (v2) to count the number of divisors of a number
def numberofdiv2(n):
    if n == 1:
        return 1
    count = 2
    for i in range(2, int(sqrt(n))):
        trial = n/float(i)
        if trial % 1 == 0:
            newn = int(trial)
            count = count + numberofdiv(newn)
            break
    return count * 2


# alternative method (v3) to count the number of divisors of a number
def numberofdiv3(n):
    count = 2
    for i in range(2,n):
        trial = n / float(i)
        if trial % 1 == 0:
            count = count + 1
    return count


# alternative method (v3) to list the number of divisors of a number
def listofdiv3(n):
    output = []
    for i in range(1,n+1):
        trial = n/float(i)
        if trial % 1 == 0:
            output.append(i)
    return output


#testing
# print numberofdiv(29160)
# print numberofdiv2(10240720)
# print numberofdiv3(10240720)
# for i in range(2,100):
#    print i, numberofdiv(i)


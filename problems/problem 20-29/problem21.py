
###
#  Problem 21 - Project Euler
#  https://projecteuler.net/problem=21
#  
#  
#  Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#  If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#  For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#  Evaluate the sum of all the amicable numbers under 10000.
#  
###

# Project Euler
# problem 21

def sumofprdiv(n):
    output=0
    if n==1:
        return 1
    for i in range(1,n):
        if (n/float(i))%1==0:
            output=output+i
    return output



total=0
done=[]
for n in range(1,10000):
    if n in done:
        continue
    dn=sumofprdiv(n)
    ddn=sumofprdiv(dn)
    if n==ddn and n!=dn:
        total = total + n + dn
        print n, dn, ddn, total
    done.append(n)
    done.append(dn)


print total

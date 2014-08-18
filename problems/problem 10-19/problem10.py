
###
#  Problem 10 - Project Euler
#  https://projecteuler.net/problem=10
#  
#
#  The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#  Find the sum of all the primes below two million.
#
#  <p class="note">Note: This problem has been changed recently, please check that you are using the right parameters.</p>
#
#
###

# Project Euler
# Problem 10

from math import sqrt

def boolprimesupto(n):
    boolprimes = [True for i in range(0,n+1)]
    boolprimes[0]=False
    boolprimes[1]=False
    for index in range(0,int(sqrt(n))+1):
        if boolprimes[index]:
            for multiples in range(index*index,n+1,index):
                boolprimes[multiples]=False
    return boolprimes



boolprimesupto2mil=boolprimesupto(2000000)

total=0
for index in range(0,len(boolprimesupto2mil)):
    if boolprimesupto2mil[index]:
        total=total+index
print total

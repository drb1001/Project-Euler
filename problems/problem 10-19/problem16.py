
###
#  Problem 16 - Project Euler
#  https://projecteuler.net/problem=16
#  
#  
#  215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#  What is the sum of the digits of the number 21000?
#  
###

# Project Euler
# problem 16

total=1
for i in range(0,100):
    total=total*1024

print total

strtotal=str(total)
sumtotal=0
for i in strtotal:
    sumtotal=sumtotal+int(i)

print sumtotal

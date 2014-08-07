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

# project euler
# problem 30

from math import pow

runningsum=0
for i in range(10,1000000):
    s=str(i)
    total=0
    for n in s:
        x=int(n)
        x5=int(pow(x,5))
        total=total+x5
    if i==total:
        print i, total
        runningsum=runningsum+i
        

print "-----------"
print runningsum


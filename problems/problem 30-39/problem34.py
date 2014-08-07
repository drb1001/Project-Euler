# project euler
# problem 34

from math import factorial

flist=[]
for i in range(0,10):
    flist.append(factorial(i))

print flist


runningsum=0
for test in range(10,3000000):
    strtest=str(test)
    total=0
    for numb in strtest:
        numb=int(numb)
        numbfact=int(flist[numb])
        total=total+numbfact
    if test==total:
        print test, total
        runningsum=runningsum+i


print "-----------"
print runningsum

# project euler
# problem 66

# x^2 - D * y^2 = 1
# (x^2 - 1)/D = y^2
# y = sqrt((x^2 - 1)/D)

# x^2 - D * y^2 = 1
# x = sqrt(1 + D * y^2)

from math import sqrt
from time import clock

start=clock()

candidates=[]
def minx(D,limit):
    if sqrt(D)%1==0:
        return -1
    y=1
    while True:
        if y>limit:
            candidates.append(D)
            return -1
        x = sqrt(1 + D * y*y)
        if x%1==0:
            return int(x)
        y+=1


max_minxD=0
oldcandidates = range(200,1001)

for limit in (10**4,10**5,10**6,10**7,10**8,10**9,10**11,10**12,10**13):
    for D in oldcandidates:
        minxD=minx(D,limit)
        if max_minxD < minxD:
           max_minxD = minxD
           print D, minxD

    print "--------"
    print len(candidates)
    print candidates[:10]
    print "--------"

    oldcandidates=candidates
    candidates=[]


print "Time: " + str(clock()-start)

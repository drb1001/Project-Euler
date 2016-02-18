# Project Euler
# Problem 26

def shortendec(n):
    output="0."
    return output


output=[]
for i in range(900,1000):
    d=1.0/i
    strd=str(d)
    print strd

    if len(strd)>11:
        if not (strd[9]==strd[10] and strd[9]==strd[11] and strd[9]==strd[12]):
            output.append(d)


print len(output)
print output



###
#  Problem 26 - Project Euler
#  https://projecteuler.net/problem=26
#
#
#  A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
#  1/2= 0.5
#  1/3= 0.(3)
#  1/4= 0.25
#  1/5= 0.2
#  1/6= 0.1(6)
#  1/7= 0.(142857)
#  1/8= 0.125
#  1/9= 0.(1)
#  1/10= 0.1
#
#  Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#  Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
#
###


def reccurcyc(d):

     #for loop - try 9, else try 9*10 + 9 else *10 +9 ...
    mult = 9.0
    l = 1
    while True:

        if mult/d % 1 == 0 : break
        else :
            mult = mult *10 + 9
            l = l+1

    return [d, 1.0/d, l]


#def longdiv(n,m):



m = [0,0]

for d in range(2,1000):
    if (d/2.0 == d/2 or d/5.0 == d/5): continue
    print reccurcyc(d)
    # mnew = reccurcyc(d)
    #if m[1] > mnew[1]:
    #    m = mnew

print m

# project euler
# problem 40

mystring=""
for i in range(1,1000001):
    mystring+=str(i)


print mystring[:30]

mycalc=1
for x in (1,10,100,1000,10000,100000,1000000):
    mycalc=mycalc*int(mystring[x-1])

print mycalc

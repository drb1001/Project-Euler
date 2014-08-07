# Project Euler
# problem 97

total=1
for i in range(0,7830457):
    if i%100000==0:
        print i
    total=(total*2)%100000000000

total=total*28433+1

print total

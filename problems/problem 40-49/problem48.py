# project euler
#problem 48

from math import pow

def power10(a,b):
    output=1
    for i in range(0,b):
        output=output*a
        if len(str(output))>12:
            output=int(str(output)[-12:])

    return output

total=0
for i in range(1,1001):
    p=power10(i,i)
    total=total+p
    print i, p, total

print total

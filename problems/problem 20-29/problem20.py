# Project Euler
# problem 20

def factorial(n):
    output=1
    for i in range(1,n+1):
        output=output*i
    return output

f100=factorial(100)
print f100

strf100=str(f100)
sumtotal=0
for i in strf100:
    sumtotal=sumtotal+int(i)

print sumtotal

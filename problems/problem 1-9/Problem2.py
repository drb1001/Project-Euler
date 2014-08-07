# Project Euler
# Problem 2

fibs=[0,1]
total=0

while True:
    next=fibs[-1]+fibs[-2]
    if next>4000000:
        break
    else:
        fibs.append(next)
        if next%2==0:
            total+=next

print total

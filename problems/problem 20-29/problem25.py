# Euler challenge
# Problem 25

a=1
b=1

count=2
while True:
    a=a+b
    count=count+1
    if len(str(a))>=1000:
        print a
        print count
        break
    
    b=b+a
    count=count+1
    if len(str(b))>=1000:
        print b
        print count
        break



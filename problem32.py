# project euler
# problem 32


for a in range(1,100):
    print a
    for b in range(1000000,999999999):
        m=a*b

        s=str(a)+str(b)+str(m)
        sarray=[]
        for letter in s:
            sarray.append(letter)
        sarray.sort()
        if s=="123456789":
            print a,b,m,s

    

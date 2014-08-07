# project euler
# problem 56

maxsum=(0,0,0)

for a in range(2,101):
    for b in range(2,101):
        absum=0
        c=a**b
        strc=str(c)
        for i in strc:
            absum=absum+int(i)
        if absum>maxsum[2]:
            maxsum=(a,b,absum)

print maxsum

# Project Euler
# problem 21

def sumofprdiv(n):
    output=0
    if n==1:
        return 1
    for i in range(1,n):
        if (n/float(i))%1==0:
            output=output+i
    return output



total=0
done=[]
for n in range(1,10000):
    if n in done:
        continue
    dn=sumofprdiv(n)
    ddn=sumofprdiv(dn)
    if n==ddn and n!=dn:
        total = total + n + dn
        print n, dn, ddn, total
    done.append(n)
    done.append(dn)


print total

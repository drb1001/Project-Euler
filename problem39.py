#project euler
#problem 39


# a + b + c = n
# a^2 + b^2 = c^2
# a <= b <= c
# a,b,c int
# c^2 = (n - (a+b))^2
# a^2 + b^2 = n^2 + (a+b)^2 - 2n(a+b)
# 0 = n^2 + 2ab - 2na - 2nb
#   = n^2 + a(2b - 2n) - 2nb
# ( 2nb - n^2)/(2b - 2n) = a
# a = (2nb-n^2)/(2b-2n)


maxncount=0
for n in range(3,1001):
    ncount=0
    for b in range (1,n):
        a = float(2*n*b-n*n)/float(2*b-2*n)
        if a%1==0 and a>0 and a<=b:
            c = n - (a+b)
            if c>0:
                ncount+=1
    if ncount>maxncount:
        maxncount=ncount
        print n,ncount


print "_________"

n=840
for b in range (1,n):
   a = float(2*n*b-n*n)/float(2*b-2*n)
   if a%1==0 and a>0 and a<=b:
       c = n - (a+b)
       if c>0:
           print int(a),int(b),int(c),int(a*a+b*b-c*c), int(a+b+c)

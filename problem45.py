# project euler
# problem 45

# tn=n(n+1)/2 = hq  =>  n^2 + n = 2hq  =>   n^2 + n - 2hq = 0
# pm=m(3m-1)/2= hq  => 3m^2 - m = 2hq  =>  3m^2 - m - 2hq = 0
# hq=q(2q-1)      

from math import sqrt


for q in range(140,100000):
    hq = q * (2*q -1)
    
    tndisc=sqrt(1 + (4*1*2*hq))
    pmdisc=sqrt(1 + (4*3*2*hq))
    
    if tndisc%1==0 and pmdisc%1==0:
        n=(-1+tndisc)/2.0
        m=(1+pmdisc)/6.0

        print q,hq,int(tndisc),int(pmdisc),n,m

        if m%1==0 and n%1==0:
            print "-----"
            print q,int(n),int(m),hq


# Project euler
# problem 413

def isddigchildno1(n):  # O(d^2)
    s=str(n)
    d=len(s)
    count=0
    for start in range(0,d):
        for end in range(start,d):  
            substring=s[start:end+1]
            if (int(substring)/float(d))%1==0:
                count+=1
            if count>1: return False
    if count==0: return False
    return True


def isddigchildno(n):
    s=str(n)
    d=len(s)
    count=0
    for length in range(1,d):
        for start in range(0,d-length+1):
            substring=s[start:start+length+1]
            if (int(substring)/float(d))%1==0:
                count+=1
            if count>1: return False
    if count==0: return False
    return True


##def isddigchildno1(n):
##    strn=str(n)
##    d=len(strn)
##    count=0
##    for mult in range(0,n,d):
##        if str(mult) in strn:
##            count+=1
##            if count>1: return False
##    if count==0: return False
##    return True


def f413(N):  #O(N)
    count=0
    for n in range(1,N):
        if n%10000==0:          
            print "  " + str(N) + " " + str(n) + " "+ str(count)
        if isddigchildno(n):
            count+=1
    return count

for N in (10,10**3,10**5):
    print N, f413(N)

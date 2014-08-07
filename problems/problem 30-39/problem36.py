# project euler
# problem 36

def ispal(s):
    l=len(s)
    if l==1: return True
    elif l==2 and s[0]==s[1]: return True
    elif l==3 and s[0]==s[2]: return True
    elif s[0]==s[l-1] and ispal(s[1:l-1]):
        return True

mysum=0
for n in range(1,1000001):
    if n%100000==0: print str(n) + "..."
    decstr=str(n)
    if ispal(decstr):
        binstr=bin(n)[2:]
        if ispal(binstr):
            mysum=mysum+n
            print decstr,binstr,mysum

print "________"
print mysum

# Euler challenge
# problem 23

def sumofprdiv(n):
    output=0
    if n==1:
        return 1
    for i in range(1,n):
        if (n/float(i))%1==0:
            output=output+i
    return output

    
perfectnum=[]
abundnum=[]
for n in range(1,25000):
    if n%1000==0:
        print n
    dn=sumofprdiv(n)
    if n==dn:
        perfectnum.append(n)
    elif n<dn:
        abundnum.append(n)
        
print "---------"        
print len(abundnum)
print "---------"

runningtotal=0
for test in range(1,25000):
    if test%1000==0:
        print test
    for abund in abundnum:
        if abund>=test:
            #print test
            runningtotal=runningtotal+test
            break
        elif (test-abund) in abundnum:
            #print test,abund,test-abund
            break
        
print "---------"
print runningtotal

            


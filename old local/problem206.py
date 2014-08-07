#project euler
#problem 206

# 1_2_3_4_5_6_7_8_9_0
# 1_2_3_4_5_6_7_8_900


from math import sqrt

minn=int(sqrt(1020304050607080900))-1
maxn=int(sqrt(1929394959697989990))+1

print minn  #1010101009
print maxn  #1389026624
1389019170

output=0

for n2 in range(13891,10100,-1):
    print n2
    for n1 in range(0,100001,10):
        n=n2*100000+n1
        strnsq=str(n*n)
        for i in range(1,10):
            if strnsq[i*2-2]!=str(i):
                break
        else:
            output=n
            print "Done: %d %d" %(n,n*n)

print "Done: %d %d" %(output,output*output)
    


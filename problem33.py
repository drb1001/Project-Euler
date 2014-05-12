# project euler
# problem 33

myfracts=[]

for den in range(10,99):
    for num in range(10,den):
        sn=str(num)
        sd=str(den)
        div=num/float(den)
        if sn[0]==sd[0] and float(sd[1])>0:
            test=float(sn[1])/float(sd[1])
            if test==div:
                print num,den
                myfracts.append([num,den])
        if sn[1]==sd[0] and float(sd[1])>0:
            test=float(sn[0])/float(sd[1])
            if test==div:
                print num,den
                myfracts.append([num,den])
        if sn[0]==sd[1] and float(sd[0])>0:
            test=float(sn[1])/float(sd[0])
            if test==div:
                print num,den
                myfracts.append([num,den])
        if sn[1]==sd[1] and float(sd[0])>0 and float(sd[1])>0:
            test=float(sn[0])/float(sd[0])
            if test==div:
                print num,den
                myfracts.append([num,den])

print myfracts

totalnum=1
totalden=1

for frac in myfracts:
    totalnum=totalnum*frac[0]
    totalden=totalden*frac[1]

print totalnum, totalden 

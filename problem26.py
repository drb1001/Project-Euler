# Euler challenge
# Problem 26

def shortendec(n):
    output="0."
    return output


output=[]
for i in range(900,1000):
    d=1.0/i
    strd=str(d)
    print strd
    
    if len(strd)>11:
        if not (strd[9]==strd[10] and strd[9]==strd[11] and strd[9]==strd[12]):
            output.append(d)


print len(output)
print output
    




def reccurcyc(d):

     #for loop - try 9, else try 9*10 + 9 else *10 +9 ...
    mult = 9.0
    l = 1
    while True:

        if mult/d % 1 == 0 : break
        else :
            mult = mult *10 + 9
            l = l+1

    return [d, 1.0/d, l]


#def longdiv(n,m):



m = [0,0]

for d in range(2,1000):
    if (d/2.0 == d/2 or d/5.0 == d/5): continue
    print reccurcyc(d)
    # mnew = reccurcyc(d)
    #if m[1] > mnew[1]:
    #    m = mnew

print m
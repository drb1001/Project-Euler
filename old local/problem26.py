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
    

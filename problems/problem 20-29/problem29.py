# Euler challenge
# problem 29

output=[]
for a in range(2,101):
    for b in range(2,101):
        c=a**b
        if c not in output:
            output.append(c)

print len(output)
        

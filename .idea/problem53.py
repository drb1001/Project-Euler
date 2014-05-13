from math import factorial

def comb_choose(n, r):
    return factorial(n) / factorial(r) / factorial(n-r)

counter = 0
for n in range(1,101):
    for r in range(1,n+1):
        if comb_choose(n, r) > 1000000:  counter = counter + 1

print counter
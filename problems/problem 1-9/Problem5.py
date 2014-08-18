
###
#  Problem 5 - Project Euler
#  https://projecteuler.net/problem=5
#
#
#  2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#  What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#
###

# Project Euler
# Problem 5


from toolbox import primefactorisation

output = []

for i in range(2,21):
    factors = primefactorisation.primefactorsarray(i)
    for n in factors:
        exists = 0
        for x in range(0,len(output)):
            o = output[x]
            if o[0] == n[0]:
                exists = 1
                if o[1] < n[1]: output[x] = n  # changing temp variable o, not output??  need to replace o in output with n
        if exists == 0: output.append(n)


print output

total = 1
for i in output:
    total = total * (i[0] ** i[1])
print total

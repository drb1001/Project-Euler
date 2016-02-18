
###
#  Problem 26 - Project Euler
#  https://projecteuler.net/problem=26
#
#
#  A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
#  1/2= 0.5
#  1/3= 0.(3)
#  1/4= 0.25
#  1/5= 0.2
#  1/6= 0.1(6)
#  1/7= 0.(142857)
#  1/8= 0.125
#  1/9= 0.(1)
#  1/10= 0.1
#
#  Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#  Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
#
###

# Project Euler
# Problem 26


# d = 2. 1/2 -> 10/2 = 5 r0. (not repeating)
# d = 3. 1/3 -> 10/3 = 3 r1. 1/3 -> 10/3 = 3 r1. (repeating, length 1)
# d = 6. 1/6 -> 10/6 = 1 r4. 4/6 -> 40/6 = 6 r4. (repeating, length 1).
# d = 7. 10/7 = 1 r 3. 30/7 = 4 r2. 20/7 = 2 r6. 60/7 = 8 r4. 40/7 = 5 r5. 50/7 = 7 r1. 10/7 is a repeat.
# d = 9. 1/9 -> 10/9 = 1 r1. 1/9-> 10/9 = 1 r1. (repeating, length 1).
# d = 11. 1/11 -> 100/11 = 9 r1. 1/11 -> 100/11 = 9 r1. (repeating, length 1).
# d = 12. 1/12 -> 100/12 = 8 r4. 4/12 -> 40/12 = 3 r4. 4/12 -> 40/12 = 3 r4. (repeating, length 1)
# d = 13. 1/13 -> 100/13 = 7 r9. 9/13-> 90/13 = 6 r12. 12/13 -> 100/13 = ...


max_rep = 0
max_n = 0
max_s = ""

for d in range(2,1000):
    output = []
    s = "0."
    rep_len = 0
    r = 1
    while True:
        while r < d: r = r*10
        len_r = len(str(r))
        q = r//d
        r = r%d

        if (r==0):
            output.append([q,r,len_r])
            rep_len = 0
            for x in output:
                s = s + str(x[0]).zfill(x[2]-1)
            break

        if ([q,r,len_r]) in output:
            p = output.index([q,r,len_r])
            #print output
            for x in output[0:p]:
                s = s + str(x[0]).zfill(x[2]-1)
            s = s + "("
            for x in output[p:]:
                s = s + str(x[0])
            s = s + ")"
            rep_len = len(output[p:])
            break

        output.append([q,r,len_r])

    print "d=%s. 1/d = %s \t (= %s) \t(rep. length = %s)" % (d, s, 1.0/d, rep_len)

    if rep_len > max_rep:
        max_rep = rep_len
        max_n = d
        max_s = s
        print "  *********"

print " -------"
print max_n, max_rep, max_s

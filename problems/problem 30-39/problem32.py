# project euler
# problem 32


for a in range(1,100):
    print a
    for b in range(1000000,999999999):
        m=a*b

        s=str(a)+str(b)+str(m)
        sarray=[]
        for letter in s:
            sarray.append(letter)
        sarray.sort()
        if s=="123456789":
            print a,b,m,s







import itertools

output = []

for i in range(123456789, 987654322):

    if notvalid(i): continue

#     test each option and add to
#
#
#
# check:
#
#
#
#
#
#
# a * b = c
#
# digits within a,b,c are digits 1-9
#
# assume a < b
#
# a 1 digit :
#
# b 1 digit => c 7 digit x
# b 2 digit => c 6 digit x
# b 3 digit => c 5 digit x
# b 4 digit => c 4 digit ?
# b 5 digit => c 3 digit x
#
#
# a 2 digit:
#
# b 1 digit => c 6 digit x
# b 2 digit => c 5 digit x
# b 3 digit => c 4 digit ?
# b 4 digit => c 3 digit x
#
#
# a 3 digit:
#
# b 1 digit => c 5 digit x
# b 2 digit => c 4 digit ?
# b 3 digit => c 3 digit x
#
#
# a 4 digit:
#
# b 1 digit => c 4 digit ?
# b 2 digit => c 5 digit ?
#
#
#
#
#

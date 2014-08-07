# Project Euler
# Problem 9


# a^2 + b^2 = {1000-(a+b)}^2
#           = 1 000 000 + (a+b)^2 - 2000(a+b)
#           = 1 000 000 + a^2 + b^2 +2ab -2000a - 2000b
# 1 000 000 =  2000a + 2000b - 2ab
#   500 000 = a(1000 - b)  + 1000b
# a = ( 500 000 - 1000b)/(1000 - b)
#   = 1000 * [ (500 - b)/(1000 - b) ]


for b in range(0,1000):
    b=float(b)
    a = 1000 * ( (500 - b)/(1000-b) )
    if a%1==0:
        c=1000-a-b
        print int(a),int(b),int(c)
        print int(b*b+a*a), int(c*c)
        print "---"

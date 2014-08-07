# Euler challenge
# problem 17

def lettercount(n):
    s=str(n)
    if len(s)==1:
        return unitsdict[n]
    if len(s)==2:
        if n in range(10,20):
            return teensdict[n]
        else:
            return tensdict[int(s[0])]+lettercount(int(s[1:])) 
    if len(s)==3:
        return lettercount(int(s[0]))+10+lettercount(int(s[1:]))
    if len(s)==4:
        return lettercount(int(s[0]))+11+lettercount(int(s[1:]))

# watch for 'and' with eg 200

        
unitsdict = {
    0:0,
    1:3,
    2:3,
    3:5,
    4:4,
    5:4,
    6:3,
    7:5,
    8:5,
    9:4
    }

teensdict = {
    10:3,
    11:6,
    12:6,
    13:8,
    14:8,
    15:7,
    16:7,
    17:9,
    18:8,
    19:8
    }

tensdict = {
    0:0,
    1:0,
    2:6,
    3:6,
    4:5,
    5:6,
    6:5,
    7:7,
    8:6,
    9:5
    }


runningcount=0
for n in range(1,1001):
    runningcount+=lettercount(n)

print runningcount    
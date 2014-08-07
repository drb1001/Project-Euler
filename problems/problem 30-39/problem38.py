# Project Euler
# Problem 38


# manually check 1 digit (1-9)
# 9 18 27 36 45 (correct)

# check 2 digits (90+)
# 91 180 270 360 (no solution - 11 digits)
# 98 196 294 392

# check 3 digits (900+)
# 912 1824 2736 (no solution - 11 digits)

# check 4 digits (90+)
for i in range(9123,9999):
    string = `i` + `i*2`
    if ''.join(sorted(string)) == "123456789" : print string

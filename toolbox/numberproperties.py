#####
# functions for checking properties of numbers
#####

# check to see if a number is a palendrome
def ispal(n):
    s = str(n)
    l = len(s)
    if l == 1 or l == 0:  return True
    elif l == 2 and s[0] == s[-1]:  return True
    elif s[0] == s[-1]:  return ispal(s[1:-1])
    else:  return False
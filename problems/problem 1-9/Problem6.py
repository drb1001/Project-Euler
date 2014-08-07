# Project Euler
# Problem 6

def sumof1to(n):
    return ((n*(n+1))//2)

def sumofsq1to(n):
    return ((n*(n+1)*((2*n)+1))//6)


print (sumof1to(100)*sumof1to(100))
print sumofsq1to(100)
print (sumof1to(100)*sumof1to(100))-sumofsq1to(100)

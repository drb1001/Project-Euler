# Project Euler
# problem 42


letterdict = {
    'A':1,
    'B':2,
    'C':3,
    'D':4,
    'E':5,
    'F':6,
    'G':7,
    'H':8,
    'I':9,
    'J':10,
    'K':11,
    'L':12,
    'M':13,
    'N':14,
    'O':15,
    'P':16,
    'Q':17,
    'R':18,
    'S':19,
    'T':20,
    'U':21,
    'V':22,
    'W':23,
    'X':24,
    'Y':25,
    'Z':26
    }


trianglenos=[]
for n in range(1,100):
    trianglenos.append( int(0.5 * n * (n+1) ) )

print trianglenos
counter=0

with open("problem42words.txt", "r") as myfile:

    mylist = myfile.read().split(",")
    for word in mylist:
        wordtotal=0
        for letter in word:
            if letter in letterdict:
                wordtotal += letterdict[letter]
        if wordtotal in trianglenos:
            counter+=1

print counter

# Project Euler
# problem 22

azdict = {
    'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,
    'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,
    'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,
    'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,
    'Z':26 }

with open('problem22names.txt','r') as myfile:
    mylist=myfile.read().split(',')

    print mylist[:100]

    mylist.sort()
    print mylist[:100]

    runningtotal=0
    position=1
    for name in mylist:
        name=name.strip('"')
        nametotal=0
        for letter in name:
            if letter in azdict:
                nametotal+=azdict[letter]
        runningtotal+=(nametotal*position)
        position+=1

print runningtotal

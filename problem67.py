

with open('problem 67 triangle.txt', 'r') as f:

    myfile = f.read().splitlines()

    myinput = []
    for x in myfile:
        myinput.append( map(int, x.split(" ")) )

    n = len(myinput)

    for l in range((n-2),-1,-1):
        for i in range(0,l+1):
            myinput[l][i] = myinput[l][i] + max( myinput[l+1][i] , myinput[l+1][i+1] )

    print myinput[0][0]


###
#  Problem 24 - Project Euler
#  https://projecteuler.net/problem=24
#  
#  
#  A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#  012   021   102   120   201   210
#  What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
#  
###


# Project Euler
# problem 24

counter = 0
numberlist = ['0','1','2','3','4','5','6','7','8','9']


for a in numberlist:
    mystr = a
    numberlist.remove(a)

    for b in numberlist:
        mystr = mystr+b
        print mystr
        numberlist.remove(b)

        for c in numberlist:
            mystr = mystr+c
            numberlist.remove(c)

            for d in numberlist:
                mystr = mystr+d
                numberlist.remove(d)

                for e in numberlist:
                    mystr = mystr+e
                    numberlist.remove(e)

                    for f in numberlist:
                        mystr = mystr+f
                        numberlist.remove(f)

                        for g in numberlist:
                            mystr = mystr+g
                            numberlist.remove(g)

                            for h in numberlist:
                                mystr = mystr+h
                                numberlist.remove(h)

                                for i in numberlist:
                                    mystr = mystr+i
                                    numberlist.remove(i)

                                    for j in numberlist:
                                        mystr = mystr+j

                                        counter = counter + 1
                                        #if counter==2000000:
                                        print counter, mystr

                                        mystr=mystr[0:-1]

                                    numberlist.insert(-1,i)
                                    mystr=mystr[0:-1]
                                    print "\t", i, counter, mystr, numberlist

                                numberlist.insert(-1,h)
                                mystr=mystr[0:-1]
                                print "\t", "\t", i, counter, mystr, numberlist

                            numberlist.insert(-1,g)
                            mystr=mystr[0:-1]

                        numberlist.insert(-1,f)
                        mystr=mystr[0:-1]

                    numberlist.insert(-1,e)
                    mystr=mystr[0:-1]

                numberlist.insert(-1,d)
                mystr=mystr[0:-1]

            numberlist.insert(-1,c)
            mystr=mystr[0:-1]

        numberlist.insert(-1,b)
        mystr=mystr[0:-1]

    numberlist.insert(-1,a)

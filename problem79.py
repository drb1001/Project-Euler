# project euler
#problem 79

with open('problem79keylog.txt','r') as myfile:
    mylist=myfile.read().split()
    mylist = list(set(mylist))
    mylist.sort()
    print mylist
    
output=mylist[0]
for code in mylist:
    if code not in output:
        if output[0] in code[1:]:
            output = code[0]+ output
        if output[-1] in code[:-1]:
            output = output + code[-1]
        test1=code[0]+code[2]
        if test1 in output:
            pos = output.find(test1)
            output = output[:pos+1] + code[1] + output[pos+1:]
        print code, output


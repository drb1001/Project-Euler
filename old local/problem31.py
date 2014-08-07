#project euler
#problem 31


runningcount=0

for a2p in range(0,2):
    runningtotal = a2p*200
    for a1p in range(0, int((200-runningtotal)/100.0) +1):
        runningtotal = a2p*200 + a1p*100
        for a50 in range(0, int((200-runningtotal)/50.0) +1):
            runningtotal = a2p*200 + a1p*100 + a50*50
            for a20 in range(0, int((200-runningtotal)/20.0) +1):
                runningtotal = a2p*200 + a1p*100 + a50*50 + a20*20
                for a10 in range(0, int((200-runningtotal)/10.0) +1):
                    runningtotal = a2p*200 + a1p*100 + a50*50 + a20*20 + a10*10
                    for a5 in range(0, int((200-runningtotal)/5.0) +1):
                        runningtotal = a2p*200 + a1p*100 + a50*50 + a20*20 + a10*10 + a5*5
                        for a2 in range(0, int((200-runningtotal)/2.0)+1 ):
                            runningtotal = a2p*200 + a1p*100 + a50*50 + a20*20 + a10*10 + a5*5 + a2*2
                            for a1 in range(0, int(200-runningtotal)+1):                
                                runningtotal = a2p*200 + a1p*100 + a50*50 + a20*20 + a10*10 + a5*5 + a2*2 + a1
                                if runningtotal==200:
                                    runningcount+=1

print runningcount
                        
                        

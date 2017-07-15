import random

boatno = 0
t= 1
totalmoney = []
returnTime = []
returntime = 0
boatmoney = 0

runningT = 0
RunningH = 0





currentT = 1111








def read():
    with open('input.txt', 'r') as f:
        lines = f.readline()
        return lines











while t == 1:
    avail = 0
    while currentT > 1000 and currentT < 1700:
        avail = 0
        currentT += 0.1
        
        currentT += 0.1
       # print currentT
        hiretype = random.randint(1,5)
        
       # if boatno < 10:
        if hiretype == 1 :
            runningT += 20
            boatmoney = 20
            RunningH += 1
            returntime = currentT + 60
            boatno += 1
            
           
        if hiretype == 2 :
            runningT += 12
            boatmoney = 12
            RunningH += 0.5
            returntime = currentT + 30
            boatno += 1
        print boatno
        #totalmoney.insert(boatno,boatmoney)
        #returnTime.insert(boatno, returntime)
        

        
        print str(boatno) +"will return at " + str(returntime) + " currebt Time is " + str(currentT)
        if boatno > 1:
            for i in range(0,len(returnTime)):
                if returnTime[i] < currentT and returnTime[i] > 0:
                    boatno -= 1
                    returnTime[i] = 0
                
                
        
        #print boatno

        if boatno  > 10:
            earliest = 9999
            for i in range (0,len(returnTime)):
                if returnTime[i] < earliest and returnTime[i] != 0:
                    earliest = returnTime[i]
            #if earliest < currentT:
                #val = returnTime.index(earliest)
                #boatno -= 1
                
                #sreturnTime.insert(val,0)
            print currentT,earliest
            


            print "earliest boat will return at " + " " + str(earliest)

        
                
        
        
            

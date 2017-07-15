import random
#defining arrays
returnTime = []
#rertun time array is used to store the return time,boatMoney  to store the money taken for each boat,trvael time store the  the total time taken on waterfor every boat
boatMoney = []
travelTime = []
boatNumber = 10
currentTime = 1001
runningT = 0
avail = 0
t = 0



#this functions simply used generate values to be input  togen rate data for the program to run on
def getHiretype():
        boatchoice = 0
        integer = random.randint(1,100)
        if integer > 60 and integer <65:
                #the probality of hiring for half an hour is hire than hiring for 1 hour
                boatchoice = 0.5
        elif integer >= 70 and integer <= 73:
                boatchoice = 1
        return boatchoice

#this is used to check whether a boat has returned and if it has incremts the number of availbale boats by  1
def checkReturn(avail):
        for i in range (0,len(returnTime)):
                #print(str(currentTime)+ " " + str(returnTime[i]))
                if returnTime[i] < currentTime:
                        
                        avail += 1
                        
                        
                        #resets the boat that arrived to return time back to zero
                        returnTime[i]=""
        return avail
                        


# fins the time the boat that will be available the fist will be available
def findReturn():
        earliest = min(returnTime)
        return earliest 


#the main loop only runs when time is below  1700 after that it stops
while currentTime > 1000 and currentTime < 1700:
        currentTime += 0.1
        

                #checks whether a boat has returned if the available number of boats is not 10
        #if boatNumber != 10:
               # boatNumber += checkReturn(avail)
        if boatNumber == 0:
                
                rtime = findReturn()
                add = checkReturn(0)
                #print add
                boatNumber += checkReturn(avail)
                print ("earliest boat that returns will return at" + " " + str(rtime)+ " ")

        HireType = getHiretype()


        if HireType == 0.5 and boatNumber > 0:
                boatMoney.insert(boatNumber,12)
                runningT += 12
                
                returnTime.insert(boatNumber,currentTime + 30)
                #ttime = time + 30
                #travelTime.insert(boatNumber,ttime)
                boatNumber -= 1
                print(boatNumber)

print runningT












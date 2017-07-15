import random
#t is use make the while loop work
t= 1
#these one dimensional array are used each indexex represents a boat
totalmoney = [0,0,0,0,0,0,0,0,0,0]
ReturnTime = [0,0,0,0,0,0,0,0,0,0]
TravelTime =[0,0,0,0,0,0,0,0,0,0]
# these two are not needed for the complete task as their values are caluculated using the values in the arrays above but necessary for first task
runningT = 0
RunningH = 0




# time in the range for easy testing
currentTime = 1111




while t == 1:
    currentTime += 1
    avail = 0
    while currentTime > 1000 and currentTime < 1700:
        #boat number set to 9 because array indexing starts  at 0
        boatnumber = 9
        #time gets incremented this way because system time cannot be used and inputing time by hand may cause problems
        currentTime += 1
        

        # caluculating available boats
        for count in range(0,10):
            #return time was printed before for debugging
            #print ReturnTime[count]
            if ReturnTime[count] > 0 and ReturnTime[count] > currentTime:  # boats number gets decremented if there is a hired boat
                boatnumber -= 1
                
        #this to was used during debugging
        #print str(boatnumber + 1) + "BOAT"
        # hiretype is found using random function currently set to between 1-3 to test make sure all boats get hired
        hiretype = random.randint(1,33)
        if boatnumber >= 0 and (hiretype == 1 or hiretype == 2):
            

            #if hire type is  1 or 2 the value of these variables are changed to efficiently enter the values into corresponding lists(arrays) 
            if hiretype == 1:
                rTime = currentTime +  60
                boatmoney = 20
                Time = 60
            
            elif hiretype == 2:
                boatmoney = 12
                Time = 30
                rTime = currentTime + 30
            #used during debugging
            #print rTime
            #the values are added to array
            totalmoney[boatnumber] = totalmoney[boatnumber] + boatmoney
            TravelTime[boatnumber] = TravelTime[boatnumber]+ Time
            ReturnTime[boatnumber] =rTime
            
        #if no boats are left shows the earliest time a boat will be available
        elif boatnumber < 0:
            earliest = 9999
            for count in range(0,10):
                # the value should be greater than zero because zero means unused boat
                if ReturnTime[count] < earliest and ReturnTime[count] > 0:
                    earliest = ReturnTime[count]
            print str(earliest) + " ealiest", currentTime


    #end of day calculations
    highest = 0
    mostused = 0
    non = 0
    daytotalmoney = 0
    daytotaltime = 0
    #the  calulations are done in for loop
    for count in range(0,10):
        daytotalmoney += totalmoney[count]
        daytotaltime += TravelTime[count]
        if TravelTime[count] > highest:
            highest = TravelTime[count]
            mostused = count + 1

        if ReturnTime[count] == 0:
            non += 1
        

    print ("Total money earned on day:" + str(daytotalmoney) + "\n"
           "Total number of time boats hired:" + str(daytotaltime) +"\n"
           "Most used Boat:" + " " + str(mostused) + "\n"
           "number of boats not used:"  + " " + str(non))
    t = 0
       
        
       
        

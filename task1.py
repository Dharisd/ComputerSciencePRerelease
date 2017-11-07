t= "y"
#these one dimensional array are used each indexex represents a boat
totalmoney = [0,0,0,0,0,0,0,0,0,0]
ReturnTime_A = [0,0,0,0,0,0,0,0,0,0]
TravelTime =[0,0,0,0,0,0,0,0,0,0]
# these two are not needed for the complete task as their values are caluculated using the values in the arrays above but necessary for first task
runningT = 0
RunningH = 0


Cost_H = 20
Cost_30 = 12
avb= 0
index = 0


while t == "y":

    avb = 0
    currentTimeHour = input("input current time HH hours")
    CurrentTimeMin = input("input current time Minutes MM")
    while int(currentTimeHour) < 10 or int(currentTimeHour) > 17:
        print("boat can only be hired between 10 and 17")
        currentTimeHour = int(input("input current time HH hours"))
        CurrentTimeMin = int(input("input current time Minutes MM"))
        
    currentTime = (int(currentTimeHour) * 60) + int(CurrentTimeMin)
    print (currentTime)



    for count in range(0,10):
        if ReturnTime_A[count] == 0:
            print("Boatnumber" + str(count + 1) + " " + " is available")
            avb += 1
        elif ReturnTime_A[count] > 0 and ReturnTime_A[count] < currentTime:
            print("Boatnumber" + str(count + 1) + " " + " is available")
            avb += 1
       
    if avb == 0:
            earliest = 9999
            for count in range(0,10):
                # the value should be greater than zero because zero means unused boat
                if ReturnTime_A[count] < earliest and ReturnTime_A[count] > 0:
                    earliest = ReturnTime_A[count]
                    index = count
            hour = int(earliest/60)
            minute =int(earliest%60)
            print ('boat'+str(index)+ " " + "arrives earliest at"+" " +str(hour)+ " "+"hours" + str(minute)+" "+ "Minutes")













    boatnumber = -1
    while boatnumber == -1:
        boatnumber = int(input("please choose a boatnumber"))
        boatnumber -= 1
        if int(ReturnTime_A[boatnumber]) > int(currentTime):
             boatnumber = -1
             print("THe boat you hired is already hired")

    
    ReturnTime = 1030
    while ReturnTime > 1020:
        HireTimeHour = int(input("input the duration of hire HH"))
        HireTimeMin = int(input("input the duration of hire in Minutes MM"))
        HireTime = (int(HireTimeHour) * 60) + HireTimeMin
        print(HireTime)
        ReturnTime = int(HireTime) + int(currentTime)
        if ReturnTime > 1020:
            print("boat should be returned before 17")
        print (ReturnTime)

    
    cost = (HireTimeHour * Cost_H) + ((HireTimeMin/30) * Cost_30)
    print (cost)


    totalmoney[boatnumber] = totalmoney[boatnumber] + cost
    TravelTime[boatnumber] = TravelTime[boatnumber]+ HireTime
    ReturnTime_A[boatnumber] = ReturnTime

























    t = input("do you want to continue(Y/N)?")

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

    if ReturnTime_A[count] == 0:
        non += 1

total_H = int(daytotaltime/60)
total_M = int(daytotaltime%60)


print ("Total money earned on day:"+"$" + str(daytotalmoney) + "\n"
        "Total number of time boats hired:" + str(total_H) + " "+"hours" +" "+ str(total_M)+" "+ "Minutes" +"\n"
        "Most used Boat:" + " " +"Boat"+ str(mostused) + "\n"
        "number of boats not used:"  + " " + str(non))
    







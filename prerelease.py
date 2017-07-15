htotal = 0
totaltime = 0
ftotal = 0
htotal = 0
btnum = 0


time = 11
t=1

while t == 1:
    time += 0.5
    if time > 10 and time < 17:

        print("1: Rent for half an hour " )
        print("2: Rent for 1 hour")
        boatchoice = input()

         #use boat choice as input
        if boatchoice == "1":
            htotal += 1
            totaltime += 0.5
            btnum += 1
            print("boat  booked for 0.5 hours")

    #if second choice is taken
        elif  boatchoice == "2":
            ftotal  += 1
            totaltime += 1
            btnum += 1
            print("boat booked for 1 hour")



    elif time >= 17:
        gtotal = (htotal * 12 + ftotal * 20)
        print("totalprofit:"+ str(gtotal))
        print("Total hours booked:" + str(totaltime))
        t = 0





































hire(11)
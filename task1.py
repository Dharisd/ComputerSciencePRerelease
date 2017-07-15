

t = 1
boatno = 1
returntime = 0 


ctime = 1001


while t == 1:
    ctime += 0.1

        
    if ctime > 1000 and ctime < 1500 and boatno >= 1:
        hiretype = input("hired?")
        if hiretype == 60:
            returntime = ctime + 60
            boatno -= 1
        if hiretype == 30:
            returntime = ctime + 30
            boatno -= 1



    

            
    else :

        
        
        print (ctime)
        print (returntime)


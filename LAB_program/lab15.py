class time:
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.min=minute
        self.sec=second
c_hour=int(input("ENter the current time\n"
                 "Hour\n"))
c_min=int(input("Minute\n"))
c_sec=int(input("second\n"))
c_time=time(c_hour,c_min,c_sec)
print("Enter the time required to make bread\n")
b_hour=int(input("HOUR\n"))
b_min=int(input("minute\n"))
b_sec=int(input("seconds\n"))
b_time=time(b_hour,b_min,b_sec)



def add():
    global finishhour
    finishhour=c_time.hour+b_time.hour
    global finishmin
    finishmin=c_time.min+b_time.min
    global finishsec
    finishsec=c_time.sec+b_time.sec
    if finishsec>59:
        finishmin+=1
        finishsec%=60
    if finishmin>59:
        finishhour+=1
        finishmin%=60
    if finishhour>12:
        finishhour%=12
def printtime():
    temphour=""
    tempmin=""
    tempsec=""
    if (len(str(finishhour)))==1:
        temphour="0"+str(finishhour)
    else:
        temphour=str(finishhour)
    if(len(str(finishmin)))==1:
        tempmin="0"+str(finishmin)
    else:
        tempmin=str(finishmin)
    if (len(str(finishsec)))==1:
        tempsec="0"+str(finishsec)
    else:
        tempsec=str(finishsec)
    print("Bread will be ready at,"+temphour+":"+tempmin+":"+tempsec)
add()
printtime()

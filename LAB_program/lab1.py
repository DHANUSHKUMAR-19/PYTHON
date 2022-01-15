def mpay(rate,h,w):
    
    pay=h*w*rate
    return pay
name=(input("Enter the name\n"))
no=input("Enter the employee id\n")
h=int(input("Enter the hours worked daily\n"))
w=int(input("Enter the total weeks worked\n"))
rate=500
pay=mpay(rate,h,w)
print("Name : \n",name,"Employee id : \n",no,"salary : \n",pay)

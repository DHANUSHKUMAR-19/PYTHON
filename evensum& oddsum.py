a=int(input("enter the total numbers going to be entered\n"))
oddsum=0
evensum=0
for i in range(a):
    b=int(input("Enter the number\n"))
    if(b%2==0):
        evensum+=b
    else:
        oddsum+=b
print("Oddsum : ",oddsum,"Evensum : ",evensum)

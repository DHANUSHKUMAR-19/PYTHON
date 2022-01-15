#FIBANOCCI NUMBERS
n=int(input("Enter the total number of terms :\t"))
f1=0
f2=1
i=0
print("\nFibanocci series : \n")
if(n==1):
    print(f1)
elif(n==2):
    print(f1)
    print(f2)
else:
    print(f1)
    print(f2)
    while(i<n-2):
        f3=f1+f2
        print(f3)
        f1=f2
        f2=f3
        i+=1

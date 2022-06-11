#Bubble sort

l1=[]
n=int(input("Enter the total numbers:"))
for i in range(n):
    a=int(input("Enter the number:"))
    l1.append(a)
print(l1)
print("Enter your choice :")
choice=int(input("1.Ascending order\n2.Descending order"))
if(choice==1):
    for i in range(n):
        for j in range(i+1,n):
            if(l1[i]>l1[j]):
                temp=l1[i]
                l1[i]=l1[j]
                l1[j]=temp
else:
     for i in range(n):
        for j in range(i+1,n):
            if(l1[i]<l1[j]):
                temp=l1[i]
                l1[i]=l1[j]
                l1[j]=temp
print("Sorted list : ",l1)

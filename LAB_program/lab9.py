def binsearch(l2,key):
    print("Sorted list:\n")
    print(l2)
    l=0
    h=len(l2)-1
    flag=0
    while(l<=h):
        mid=(l+h)//2
        if(key==l2[mid]):
            flag=1
            break
        elif key>l2[mid]:
            l=mid+1
        else:
            h=mid-1
    if(flag==0):
        return 0
    else:
        return mid+1
l1=[]
l2=[]
n=int(input("Enter the total numbers\n"))
for i in range(n):
    a=int(input(""))
    l1.append(a)
l1.sort()
print(l1)
key=int(input("Enter the key element to search\n"))
pos=binsearch(l1,key)
if(pos==0):
    print("element doesnot founf\n")

else:
    print("Element is found at pos :",pos)

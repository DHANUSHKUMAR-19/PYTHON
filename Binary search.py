def binr(l1,key):
    flag=0
    l=0
    h=n-1
    while l<=h:
        mid=l+h//2
        if key==l1[mid]:
            flag=1
            break
        elif key<l1[mid]:
            h=mid-1
        else:
            l=mid+1
    if flag==0:
        return 0;
    else:
        return mid+1;
l=[]
n=int(input("enter the total numbers going to be entered\n"))
for i in range(n):
    num=int(input("Enter the number %d\n"%(i+1)))
    l.append(num)
l.sort()
l2=sorted(l1,reverse=true)
print(l2)
key=int(input("ENter the elemnet to found\n"))
ans=binr(l,key)
if ans==0:
    print("Key not found")
else:
    print(ans)

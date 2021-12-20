l1=[]
n=int(input("Enter the total numbers going to be entered\n"))
for i in range(n):
    a=int(input("Enter %d number"%(i+1)))
    l1.append(a)
ch=int(input("enter your choice\n"))
if ch==1:
    for i in range(n):
        for j in range(i+1,n):
            if l1[i]>l1[j]:
                temp=l1[i]
                l1[i]=l1[j]
                l1[j]=temp
else:
  for i in range(n):
        for j in range(i+1,n):
            if l1[i]<l1[j]:
                temp=l1[i]
                l1[i]=l1[j]
                l1[j]=temp
print("sprted elemnets are\n")
print(l1)

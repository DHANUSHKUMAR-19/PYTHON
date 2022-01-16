l1=[]
l2=[]
def bubble(n,l1,ch):
    temp=0
    if(ch==1):
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
    return l1
        
    
l1=[]
l2=[]
n=int(input("ENter the total number to be entered\n"))
for i in range(n):
    a=int(input(""))
    l1.append(a)
ch=int(input("1.ascending\n2.decending"))
if(ch==1):
    l2=bubble(n,l1,ch)
elif(ch==2):
    l2=bubble(n,l1,ch)
else:
    print("invalid choice\n")
    
print("sorted list\n")
print(l2)

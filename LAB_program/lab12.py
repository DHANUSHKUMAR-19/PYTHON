def index(l2):
    samll=l2.index(min(l2))
    return samll
n=int(input("ENter the number\n"))
l1=[]
for i in range(n):
    a=int(input(""))
    l1.append(a)
small=index(l1)
print("index of samllest element is : ",small)

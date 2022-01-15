def indexOfSmallestElement(lst):
    smallest=lst.index(min(lst))
    return smallest
lst=[]
n=int(input("ENter the numbers\n"))
for i in range(n):
    a=int(input(""))
    lst.append(a)
sm=indexOfSmallestElement(lst)
print("THe list is : ")
print(lst)
print("min index : ",sm)

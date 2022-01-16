class rectangle:
    def __init__(self,h,w):
        self.h=h
        self.w=w
    def getarea(self):
        return self.h*self.w
l1=[]
l2=[]
n=int(input("Enter the no of tottal rectangles\n"))
for i in range(n):
    print("Rectangle :",i+1)
    h=int(input("Enter the height\n"))
    w=int(input("Enter the width\n"))
    l1.append(rectangle(h,w))
    l2.append(l1[i].getarea())
print("Max rectangle\n")
print("Area :\t",max(l2),"Height : \t",l1[l2.index(max(l2))].h,"Width : \t",l1[l2.index(max(l2))].w)
print("Minimum rectangle\n")
print("Area : \t",min(l2),"Height : \t",l1[l2.index(min(l2))].h,"width : \t",l1[l2.index(min(l2))].w)

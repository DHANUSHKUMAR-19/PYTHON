class country:
    def __init__(self,country,capital,pop):
        self.country=country
        self.cap=capital
        self.pop=pop
    def display(self):
        print("\ncountry :",self.country,"\tcapital :",self.cap,"\tPopulation :",self.pop)
    def popul(self):
        return self.pop
l1=[]
l2=[]
l3=[]
f=True
while(f):
    ch=int(input("\n1.Create\n2.Search\n3.Max pop\n4.Exit\n"))
    if ch==1:
        cntry=input("Enter the country name\n")
        if cntry in l2:
            print("Country name already exists\n")
        else:
            cap=input("Enter the capital\n")
            pop=int(input("Enter the population\n"))
            l1.append(country(cntry,cap,pop))
            l2.append(cntry)
    elif ch==2:
        cntry=input("Enter the country name :\n")
        if cntry in l2:
            l1[l2.index(cntry)].display()
        else:
            print("Country name doesn't exists\n")
    elif ch==3:
        for i in l2:
            l3.append(l1[l2.index(i)].popul())
        print("country with max population :\n")
        l1[(l3.index(max(l3)))].display()
    elif ch==4 :
        f=False
    else:
        print("Invalid choice\n")
            

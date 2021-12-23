class world:
    def __init__(self,country,population,capital):
        self.country=country
        self.population=population
        self.capital=capital
    def population(self):
        print("Country :\n",self.country,"Capital :\n",self.capital,"Population :\n",self.population)
    def popl(self):
        return self.population    
l1=[]
l2=[]
l3=[]
n=0
f=True
while(f):
    try:
        n=int(input("\n1.Add\n2.search\n3.Display\n"))
    except:
        print("Please enter a Number\n")
    if(n==1):
        
     cnt=input("\nEnter the country name\n")
     if cnt in l2:
         print("Country already exists\n")
     else:
      cap=input("Enter the capital\n")
      pop=int(input("Enter the population\n"))
      l1.append(world(cnt,pop,cap))
      l2.append(cnt)
    elif n==2:
        try:
            cnt=input("Enter country name\n")
            i=l2.index(cnt)
            print("The pop : ",l1[i].popl())
            l1[i].population()
        except:
            print("Country not found\n")
    elif(n==3):
        try:
            for i in len(l2):
                l3.append(l2[i])
            print(l3)
            print("Max population country : ",l2[l3.index(max(l3))])
            print("Max population: ",max(l3))
        except:
            print("No countries entered\n")
    else:
        f=False
   
        

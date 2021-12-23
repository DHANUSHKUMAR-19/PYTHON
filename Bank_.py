class account:
    def __init__(self,acc):
        self._acc=acc
        self._balance=0
    def deposit(self,amt):
        self._balance+=amt
    def withdraw(self,amt):
        if(self._balance-amt>100):
            print("Successfull withdraw\n")
        else:
            print("Insufficient Balance\n")
    def display(self):
       return self._balance
l1=[]
l2=[]
l3=[]
am=0
f=True
while(f):
    print("\n1.Create\n2.Deposit\n3.withdraw\n4.Display\n5.Max balance\n6.Toal Bank Balance\n7.Exit\n")
    n=int(input("Enter  your choice\n"))
    if(n==1):
        acc=int(input("Enter the account number\n"))
        if acc in l2:
            print("Account already exists\n")
        else:
            l1.append(account(acc))
            l2.append(acc)
            print(l2)
    elif(n==2):
        acc=int(input("Enter the account number : \n"))
        try:
            i=l2.index(acc)
            amt=int(input("Enter the acoount number\n"))
            am+=amt
            l1[i].deposit(amt)
            
        except:
            print("Account number doesn't to exist\n")
    elif(n==3):
        acc=int(input("Enter the account number\n"))
        try:
            i=l2.index(acc)
            amt=int(input("Enter the amount to withdraw\n"))
            am-=amt
            l1[i].withdraw(amt)
        except:
            print("Account doesn't exist\n")
    elif(n==4):
        acc=int(input("Enter the account number\n"))
        try:
            i=l2.index(acc)
            print(i)
            print("Total balance : ",l1[i].display())
        except:
            print("Account doesn't exists\n")
    elif(n==5):
        for i in range(len(l2)):
            l3.append(l1[i].display())
        i=l3.index(max(l3))
        print("Account number : ",l2[i],"Balance : ",l3[i])
    elif(n==6):
        print("The total Bank balance :",am)
    else:
        f=False
            

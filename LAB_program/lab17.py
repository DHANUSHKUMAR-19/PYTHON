class account:
    def __init__(self,acc):
        self._accno=acc
        self._balance=100
    def deposit(self,amt):
        self._balance+=amt
    def withdraw(self,amt):
        if(self._balance-amt)>100:
            print("Successfull witdraw\n")
            self._balance-=amt
        else:
            print("insufficient balance\n")
    def getbalance(self):
        return self._balance
l1=[]
l2=[]
l3=[]
f=True
while(f):
    ch=int(input("\n1.Create Account\n2.Deposit\n3.Withdraw\n4.Max Balance\n5.Exit\n"))
    if ch==1:
        acc=int(input("Enter the account number\n"))
        if acc in l2:
            print("acount number already exists\n")
        else:
            l1.append(account(acc))
            l2.append(acc)
    elif ch==2:
        acc=int(input("Enter the account number\n"))
        if acc in l2:
            amt=int(input("Enter the amount to deposit\n"))
            l1[l2.index(acc)].deposit(amt)
        else:
            print("Acoount doesn't exists\n")
    elif ch==3:
        acc=int(input("Enter the account number\n"))
        if acc in l2:
            amt=int(input("Enter the balance to withdraw\n"))
            l1[l2.index(acc)].withdraw(amt)
        else:
            print("Account doesn't exists\n")
    elif ch==4:
        for i in l2:
            l3.append(l1[l2.index(i)].getbalance())
        print("Max balance account number is : ",l2[l3.index(max(l3))])
        print("Max account balance is : ",max(l3))
    elif ch==5:
        f=False
    elif ch==6:
        acc=int(input("Enter the account number\n"))
        if  acc in l2:
            print("Your account balance is : \t",l1[l2.index(acc)].getbalance())
    else:
        print("Account doesn't exists\n")
        print("Invalid choice\n")

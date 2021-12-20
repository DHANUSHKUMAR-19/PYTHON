import sys
class bank:
    def __init__(self,balance,name):
        self.balance=balance
        self.name=name
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        if(self.balance<amount):
            print("Insuffiecient balance\n")
            return self.balance
        else:
            self.balance-=amount
            return self.balance
    def display(self):
        return self.balance

name=input("Enter your name\n")
balance=0
s=bank(balance,name)
while(1):
    print("\n1.Deposit\n2.Withdraw\n3.Check balance\n4.Exit\n")
    ch=int(input("Enter your choice\n"))
    if(ch==1):
        b=int(input("Enter the amount to deposit\n"))
        print("Your current Balance is : ",s.deposit(b))
    elif(ch==2):
        c=int(input("Enter the amount to withdraw\n"))
        print("Your Existing balance is : ",s.withdraw(c))
    elif(ch==3):
        print("Your Balance is :",s.display())
    else:
        sys.exit(0)
            
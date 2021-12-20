employeeid=int(input("Enter your employee id\n"))
basicsalary=int(input("Enter your slary\n"))
allowance=int(input("Enter your allowance\n"))
gross=allowance+basicsalary
if gross>20000:
    tax=gross*.3
elif gross>10000:
    tax=gross*.2
elif gross>5000:
    tax=gross*.1
else:
    tax=0
netsalary=gross-tax
print("netsalary : ",netsalary)

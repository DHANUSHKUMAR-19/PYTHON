name=input("ENter your name :\n")
ba=int(input("ENter your basic salary\n"))
al= .2*ba
gs=al+ba
tax=0
if gs>20000:
    tax=gs*.3
elif gs>10001 and gs<20000:
    tax=gs*.2
elif gs>50001 and gs<10000:
    tax=gs*.1
else:
    tax=0
ns=gs-tax
print("Net salar : \n",ns)

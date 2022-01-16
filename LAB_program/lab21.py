from tkinter import *
from math import *
def calculate():
    a=float(t1.get())
    b=float(t2.get())
    c=float(t3.get())
    mr=(c/100)/12
    fval=a*pow(1+mr,b*12)
    print(fval)
    l5.configure(text=fval)



    
root=Tk()
root.title("Investment calculator\n")

l1=Label(root,text="Investment Amount")
l1.grid(row=0)
l2=Label(root,text="Year")
l2.grid(row=1)
l3=Label(root,text="Annual interest rate")
l4=Label(root,text="Future value ")
l4.grid(row=3)
l3.grid(row=2)
l5=Label(root)
l5.grid(row=3,column=1)
t1=Entry(root,width=20)
t1.grid(row=0,column=1)
t2=Entry(root,width=20)
t2.grid(row=1,column=1)
t3=Entry(root,width=20)
t3.grid(row=2,column=1)
b1=Button(text="CALCULATE",command=calculate)
b1.grid(row=4,column=1)
root.mainloop()

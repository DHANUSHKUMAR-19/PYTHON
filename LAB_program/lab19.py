from tkinter import *
from tkinter import messagebox
def add():
    a=float(e1.get())
    b=float(e2.get())
    sum1=a+b
    messagebox.showinfo("result","sum of two number is : %.2f"%sum1)
def sub():
    a=float(e1.get())
    b=float(e2.get())
    sub=a-b
    messagebox.showinfo("result","substraction of two number is : %.2f"%sub)
def mul():
    a=float(e1.get())
    b=float(e2.get())
    mul=a*b
    messagebox.showinfo("result","Multiplication of two number is :%.2f "%mul)
def div():
    a=float(e1.get())
    b=float(e2.get())
    if(b==0):
        messagebox.showinfo("result","division by zero is not allowed")
    else:
        div=a/b
        messagebox.showinfo("result","Division of two numbers is : %.2f"%div)
root=Tk()
root.geometry("450x450")
root.title("Calculator")
l1=Label(root,text="Enter value 1: ",font=('calibri',25,'bold'))
l2=Label(root,text="Enter value 2: ",font=('calibri',25,'bold'))
l1.grid(row=0)
l2.grid(row=1)
e1=Entry(root,width=20,borderwidth=5,font=('calibri',15,'bold'))
e2=Entry(root,width=20,borderwidth=5,font=('calibri',15,'bold'))
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
b1=Button(root,text='+',command=add,width=10)
b2=Button(root,text='-',command=sub,width=10)
b3=Button(root,text='*',command=mul,width=10)
b4=Button(root,text='/',command=div,width=10)
b5=Button(root,text='exit',command=exit,width=10)
b1.grid()
b2.grid()
b3.grid()
b4.grid()
b5.grid()




from tkinter import *
import sys
from tkinter import messagebox
def add():
    a=float(T1.get())
    b=float(T2.get())
    sum=a+b
    messagebox.showinfo("Result","Sum of two numbers =%.2f\n"%sum)
def sub():
    a=float(T1.get())
    b=float(T2.get())
    sub=a-b
    messagebox.showinfo("Result","sub of two numbers =%.2f\n"%sub)
def mul():
    a=float(T1.get())
    b=float(T2.get())
    mul=a*b
    messagebox.showinfo("Result","Multiplication of two numbers =%.2f\n"%mul)
def div():
    a=float(T1.get())
    b=float(T2.get())
    if(b==0):
        messagebox.showinfo("Division by zero is not allowed\n")
    else:
        div=a/b
        messagebox.showinfo("Result","Division of two numbers =%.2f\n"%div)
root=Tk()
root.geometry("450x450")
lb1=Label(root,text="Enter  a value  ")
lb1.grid(row=0)
lb2=Label(root,text="Enter a value ")
lb2.grid(row=1)
T1=Entry(root,width=55,borderwidth=5)
T1.grid(row=0,column=1)
T2=Entry(root,width=55,borderwidth=5)
T2.grid(row=1,column=1)
e1=Button(root,text="ADD",command=add)
e2=Button(root,text="SUB",command=sub)
e3=Button(root,text="MUL",command=mul)
e4=Button(root,text="DIV",command=div)
e5=Button(root,text="Exit",command=exit)
e1.grid()
e2.grid()
e3.grid()
e4.grid()
e5.grid()

root.mainloop()

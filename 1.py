from tkinter import*
root=Tk()
root.title("MY CALCULATOR")
root.geometry("312x324")
#functions
def btn_click(item):
    global expression
    expression+=str(item)
    input_text.set(expression)
def btn_clear():
    global expression
    expression=""
    input_text.set("")
def btn_equal():
    global expression
    result=str(eval(expression))
    input_text.set(result)
    expression=""
input_text=StringVar()
expression=""
#input frame
input_frame=Frame(root,width=312,height=60,highlightcolor='black',highlightbackground='black',highlightthickness=2)
input_frame.pack(side='top')
input_field=Entry(input_frame,width=312,bd=10,bg='#eee',textvariable=input_text,font=('aerial',18,'bold'),justify="right")
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)
btn_frame=Frame(root,width=312,height=272.5,bg="grey")
btn_frame.pack()
clear=Button(btn_frame,width=32,height=3,bd=0,fg="black",text="C",bg="#eee",command=lambda:btn_clear()).grid(row=0,column=0,columnspan=3,padx=1,pady=1)
divide=Button(btn_frame,width=10,height=3,bd=0,fg="black",text="/",bg="#eee",command=lambda:btn_click('/')).grid(row=0,column=3,padx=1,pady=1)
seven=Button(btn_frame,width=10,height=3,bd=0,fg='black',text="7",bg='#fff',command=lambda:btn_click(7)).grid(row=1,column=0,padx=1,pady=1)
eight=Button(btn_frame,width=10,height=3,bd=0,fg='black',text="8",bg='#fff',command=lambda:btn_click(8)).grid(row=1,column=1,padx=1,pady=1)
nine=Button(btn_frame,width=10,height=3,bd=0,fg='black',text="9",bg='#fff',command=lambda:btn_click(9)).grid(row=1,column=2,padx=1,pady=1)
mul=Button(btn_frame,width=10,height=3,bd=0,fg='black',text="*",bg='#fff',command=lambda:btn_click('*')).grid(row=1,column=3,padx=1,pady=1)
equal=Button(btn_frame,width=44,height=3,bd=0,bg='#eee',text="=",fg="black",command=lambda:btn_equal()).grid(row=2,column=0,columnspan=4,padx=1,pady=1)

root.mainloop()

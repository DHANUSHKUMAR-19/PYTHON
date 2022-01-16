from tkinter import *

root=Tk()
root.title("MY CALCULATOR")
root.geometry("312x324")
#creating functions
def btn_click(item):
    global expression
    expression+=str(item)
    input_text.set(expression)
def clear_btn():
    global expression
    expression=""
    input_text.set("")
def btn_equal():
    global expression
    result=str(eval(expression))
    input_text.set(result)
    expression =""
expression=""
input_text=StringVar()
input_frame=Frame(root,height=60,width=312,highlightcolor='black',highlightbackground='black',highlightthickness=2)
input_frame.pack(side=TOP)
input_field=Entry(input_frame,width=312,font=('aerial',18,'bold'),textvariable=input_text,bd=0,bg="#eee",justif="right")
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)
#BUTTONS
btn_frame=Frame(root,width=312,height=272.5,bg="grey")
btn_frame.pack()
clear=Button(btn_frame,text="C",fg='black',bd=0,bg="#eee",width=32,height=3,cursor='hand2',command=lambda:clear_btn()).grid(row=0,column=0,padx=1,pady=1,columnspan=3)
divide = Button(btn_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
seven=Button(btn_frame,text="7",bg="#fff",bd=0,fg='black',width=10,height=3,command=lambda:btn_click(7)).grid(row=1,column=0,padx=1,pady=1)
eight=Button(btn_frame,text="8",bg="#fff",bd=0,fg='black',width=10,height=3,command=lambda:btn_click(8)).grid(row=1,column=1,padx=1,pady=1)
nine=Button(btn_frame,text="9",bg="#fff",bd=0,fg='black',width=10,height=3,command=lambda:btn_click(9)).grid(row=1,column=2,padx=1,pady=1)
mul=Button(btn_frame,text="*",bg="#eee",bd=0,fg='black',width=10,height=3,command=lambda:btn_click('*')).grid(row=1,column=3,padx=1,pady=1)

#second row
four=Button(btn_frame,text="4",bg="#fff",bd=0,fg='black',width=10,height=3,command=lambda:btn_click(4)).grid(row=2,column=0,padx=1,pady=1)
five=Button(btn_frame,width=10,height=3,bd=0,text='5',bg='#fff',fg='black',command=lambda:btn_click(5)).grid(row=2,column=1,padx=1,pady=1)
six=Button(btn_frame,width=10,height=3,bd=0,text='6',bg='#fff',fg='black',command=lambda:btn_click(6)).grid(row=2,column=2,padx=1,pady=1)
add=Button(btn_frame,width=10,height=3,bd=0,text='+',bg='#eee',fg='black',command=lambda:btn_click('+')).grid(row=2,column=3,padx=1,pady=1)
#3rd row
one=Button(btn_frame,text="1",bg="#fff",bd=0,fg='black',width=10,height=3,command=lambda:btn_click(1)).grid(row=3,column=0,padx=1,pady=1)
two=Button(btn_frame,text="2",bg="#fff",bd=0,fg='black',width=10,height=3,command=lambda:btn_click(2)).grid(row=3,column=1,padx=1,pady=1)
three=Button(btn_frame,text="3",bg="#fff",bd=0,fg='black',width=10,height=3,command=lambda:btn_click(3)).grid(row=3,column=2,padx=1,pady=1)
minus=Button(btn_frame,text="-",bg="#eee",bd=0,fg='black',width=10,height=3,command=lambda:btn_click('-')).grid(row=3,column=3,padx=1,pady=1)
#4th row
zero=Button(btn_frame,text="0",bg="#fff",bd=0,fg='black',width=21,height=3,command=lambda:btn_click(0)).grid(row=4,column=0,columnspan=2,padx=1,pady=1)
dot=Button(btn_frame,text=".",bg="#eee",bd=0,fg='black',width=10,height=3,command=lambda:btn_click('.')).grid(row=4,column=2,padx=1,pady=1)
equal=Button(btn_frame,text="=",bg="#eee",bd=0,fg='black',width=10,height=3,command=lambda:btn_equal()).grid(row=4,column=3,padx=1,pady=1)


root.mainloop()


from tkinter import *
root=Tk()
root.title("SIMPLE CALCULATOR")
root.geometry("425x450")

field=Entry(root,width=60)
field.grid(row=0,column=1,columnspan=3,padx=20,pady=10)
root.mainloop()

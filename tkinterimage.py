from tkinter import *
root=Tk()
root.geometry("455x244")
#how to add jpg
image=Image.open("pic.jpg")
photo=ImageTk.PhotoImage(image)
phot.pack()
# p=PhotoImage(file="pic.jpg")
l=Label(image=p)
l.pack()
root.mainloop()
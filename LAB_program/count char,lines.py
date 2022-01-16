import sys,os
fname=input("Enter the file name :\t")
cc=cw=cl=0
if os.path.isfile(fname):
    with open(fname,'r') as f:
        for i in f:
            word=i.split()
            cw+=len(word)
            cc+=len(i)
            cl+=1
    print("words : ",cw,"lines : ",cl,"characters : ",cc)
else:
    print("file doesn't exists\n")

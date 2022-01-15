import os,sys
fname=input("Enter the file name\n")
cl=cw=cc=0
if os.path.isfile(fname):
    with open(fname,'r') as f:
        for line in f:
            word=line.split()
            cw+=len(word)
            cc+=len(line)
            cl+=1
    print(":",cc)
else:
    print("File doesnot exists\n")

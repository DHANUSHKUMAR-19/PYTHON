import os,sys
fname=input("Enter the file name\n")
if os.path.isfile(fname):
    f=open(fname,'r')
else:
    print("File doesn't exitsts\n")
    sys.exit()
cc=cw=cl=0
for line in f:
    word=line.split()
    print(word)
    print(len(word))
    cl+=1
    cw+=len(word)
    cc+=len(line)

print(word)
print("\nThere are %d lines"%cl,"\nThere are %d charatcters\n"%cc,"There are %d words"%cw)
    

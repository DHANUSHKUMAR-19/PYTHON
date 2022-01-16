import os
fname=input("Enter the file name:\t")
total =0
if os.path.isfile(fname):
        with open(fname,'r') as f:
            for i in f:
                mark=i.split()
                print(mark)
                for j in range(len(mark)):
                    total+=int(mark[j])
                print("total marks = ",total)
                print("Average = ",total/len(mark))
                total=0
else: 
    print("file doesnot exists\n")

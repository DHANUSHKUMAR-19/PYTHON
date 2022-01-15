fname=input("Enter the file name\n")
j=0
try:
 with open(fname,'r') as f:
    total=0
    for line in f:
        mark=line.split()
        print(mark)
        for i in range(len(mark)):
            total+=int(mark[i])
        j+=1
        print("student : ",j)
        print("total marks : ",total)
        print("average marks :",total/(len(mark)))
        total=0
except:
    print("File not found\n")

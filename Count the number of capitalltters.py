name=input("enter the string\n")
count=0
n=len(name)
for i in range(n):
    if name[i].isupper():
        print(name[i])
        count+=1
print("there are %d capital letters"%count)

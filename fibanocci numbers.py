f1=0
f2=1
a=int(input("enter the ending number\n"))
print(f1)
print(f2)
for i in range(a-2):
    f3=f1+f2
    print(f3)
    f1=f2
    f2=f3

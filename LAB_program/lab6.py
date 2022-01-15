d1={'a':0,'e':0,'i':0,'o':0,'u':0}
s1=input("Enter the string\n")
for i in s1:
    if i in d1:
        d1[i]+=1
print(d1)

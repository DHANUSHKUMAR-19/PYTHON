s1=input("Enter the string\n")
#dict1={'a':0,'e':0,'i':0,'o':0,'u':0}
dict2={'a':0,'b':0}
for i in s1:
    if i in dict2:
        dict2[i]+=1
print(dict2)

s1=input("Enter the string 1\n")
s2=input("Enter the string2\n")
s3=""
for i in s1:
    if i.isupper():
        s3+=i
for j in s2:
    if j.isupper():
        s3+=j
print(s3)

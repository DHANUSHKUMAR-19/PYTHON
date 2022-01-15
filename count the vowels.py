str1=['a','e','i','o','u']
str2=input("Enter the string\n")
n=len(str2)
count=0
for i in range(n):
    if str2[i] in str1:
        print(str2[i])
        count+=1
print("count=%d\n"%count)

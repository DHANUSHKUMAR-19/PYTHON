a={}
n=int(input("Enter the total numbers\n"))
for i in range(n):
 key=input("Enter your name\n")
 value=int(input("Enter your marrks\n"))
 a[key]=value
b=sorted(a,key=a.get,reverse=True)
print("Top 3 scores are\n")
for i in b[ :3]:
     print(i ,":" ,a[i])




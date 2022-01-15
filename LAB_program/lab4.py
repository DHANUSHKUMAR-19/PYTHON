d1={"john":86.5,"jack":91.2,"jill":84.5,"harry":72.1,"joe":80.5}
l2=[]
avg=0
l2=sorted(d1,key=d1.get,reverse=True)
print("Top 3 scorers are :\n")
for i in l2[0:3]:
    print(i ,":",d1[i])
for i in d1:
    avg+=d1[i]
print("average score : %.2f\n"%(avg//len(d1)))
    
    
    

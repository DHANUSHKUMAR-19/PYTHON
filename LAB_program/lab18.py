key=open('keys.txt','r').readline().split()
mark=open('marks.txt','r')
mark_list=[]
name_list=[]
for line in mark:
    t=line.split()
    name=t[0]
    count=0
    for i in range(1,len(key)):
        print(t[i],key[i])
        if t[i]==key[i]:
            count+=1
    print(name,"scored",count,"/10")
    mark_list.append(count)
    name_list.append(name)
top=max(mark_list)
x=mark_list.index(top)
print("Top scorer\n")
#n=name_list[x]
print(name_list[x],"scored",top,"/10")


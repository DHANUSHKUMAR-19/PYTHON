a=[[1,2,3],
   [3,4,6],
   [5,8,9]]
tp=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
                tp[j][i]=a[i][j]
for i in tp:
    print(i)

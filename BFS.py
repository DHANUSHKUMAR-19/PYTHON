from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)
    def BFS(self,s):
        print("lenght of graph=",len(self.graph))
        visited=[False]*(100)
        queue=[]
        queue.append(s)
        visited[s]=True
        while queue:
            s=queue.pop(0)
            print(s,end="-")
            for i in self.graph[s]:
                if visited[i]==False:
                 queue.append(i)
                 visited[i]=True
#driver code
g=Graph()
n=int(input("Enter the total edges: "))
for i in range(n):
    u=int(input("Enter the starting vertex:"))
    v=int(input("Enter the ending vertex: "))
    g.addedge(u,v)
s=int(input("Enter the starting addres:"))
g.BFS(s)

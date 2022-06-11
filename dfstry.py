from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)
    def dfs(self,s,visited):
        print(s,end="-->")
        visited.add(s)
        for i in self.graph[s]:
            if i  not in visited:
                self.dfs(i,visited)
              
g=Graph()
n=int(input("Enter the total edges: "))
for i in range(n):
    u=int(input("Enter the starting vertex:"))
    v=int(input("Enter the ending vertex: "))
    g.addedge(u,v)
visited=set()
s=int(input("Enter the start vertex:"))
print( "Following is Depth First Traversal")
g.dfs(s,visited)

        
        

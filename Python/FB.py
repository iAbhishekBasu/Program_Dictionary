from collections import defaultdict

class Graph:
 
    # Constructor
    def __init__(self,n):
        self.graph = defaultdict(list)
        self.V=n
 
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
 
    # BFS Traversal
    def friend_recommendation(self, s , visited):
        queue = []
        queue.append(s)
        visited[s] = True
        recommendations=[]

        for distance in range(0,2,1):
          for iterate in range(0,len(queue),1):
            node = queue.pop(0)
            for i in self.graph[node]:
              if (distance==1 and visited[i] == False) :
                recommendations.append(i)
              if visited[i] == False:
                queue.append(i)
                visited[i] = True
        if recommendations:
          print("Friend Recommendations for person are" ,recommendations)
        else:
          print("There are no recommendations based on the network")


    def BFS(self,node):
      visited = [False] * self.V
      self.friend_recommendation(node,visited)

n=int(input(("Enter total number of persons in the network.")))
g=Graph(n)
e=int(input(("Enter total number of edges in the network.")))
print("Enter the friend pairs.")
for i in range(0,e,1):
  u,v=[int(x) for x in input().split()]
  g.add_edge(u,v)
person=int(input(("Enter the person whose friend recommendations is to be found.")))
g.BFS(person)

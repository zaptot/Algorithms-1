#!/usr/bin/env python
# coding: utf-8

# In[25]:


from collections import defaultdict 
   
class Graph: 
   
    def __init__(self,vertices): 
        self.V= vertices
        self.graph = defaultdict(list)
        self.Time = 0
   
    def addEdge(self): 
        print('Введите вершины ребра: ')
        u=(int(input()))
        v=(int(input()))
        self.graph[u].append(v) 
        self.graph[v].append(u)
        
    def DFS(self):
        time = 0
        graph = self
        visited = [False] * (self.V) 
        disc = self.V
        low = self.V
        parent = self.V
        articulationPoints = [False] * (self.V) 
        for i in range(self.V):
            parent[i] = -1
            visited[i] = False
            articulationPoints[i] = False
        return articulationPoints

    def findArticulationPoints():
        points = []
        for i in range (self.V):
            if (articulationPoints[i]):
                print((i + 1) + " ")
                points.append(i)
        return points
        
    def isBCUtil(self, u, visited, parent, low, disc): 
        children =0
        visited[u]= True
        disc[u] = self.Time 
        low[u] = self.Time
        self.Time += 1
        for v in self.graph[u]:
            if visited[v] == False : 
                parent[v] = u 
                children += 1
                if self.isBCUtil(v, visited, parent, low, disc): 
                    return True
                low[u] = min(low[u], low[v])
                if parent[u] == -1 and children > 1: 
                    return True
                if parent[u] != -1 and low[v] >= disc[u]: 
                    return True    
                      
            elif v != parent[u]:
                low[u] = min(low[u], disc[v]) 
  
        return False

    def isBC(self):
        articulationPoints = self.DFS()
        visited = [False] * (self.V) 
        disc = [float("Inf")] * (self.V) 
        low = [float("Inf")] * (self.V) 
        parent = [-1] * (self.V)
        flag = True
        for i in range (self.V):
            if (not visited[i]):
                self.isBCUtil(i, visited, parent, low, disc)
        for articulationPoint in articulationPoints:
            if (articulationPoint):
                flag = False
        for i  in range (self.V):
            if (not visited[i]):
                return False
        return flag


# In[27]:


# Задание графов(матрица инцидентности)
N = int(input('Ведите количество вершин: '))

graph=Graph(N)

print("Хотите добавить ребра? y/n ")
agree=str(input())
while(agree=="y"):
    graph.addEdge()
    agree=str(input("Ввести еще ребро? y/n "))
print ("Yes" if graph.isBC() else "No")


# In[ ]:





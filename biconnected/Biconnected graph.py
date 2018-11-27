#!/usr/bin/env python
# coding: utf-8

# In[10]:


from collections import defaultdict 
   
class Graph: 
   
    def __init__(self,vertices): 
        self.V= vertices
        self.graph = defaultdict(list)
        self.Time = 0
   
    # function to add an edge to graph 
    def addEdge(self): 
        print('Введите вершины ребра: ')
        u=(int(input()))
        v=(int(input()))
        self.graph[u].append(v) 
        self.graph[v].append(u)
        
    def isBCUtil(self,u, visited, parent, low, disc): 
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
        visited = [False] * (self.V) 
        disc = [float("Inf")] * (self.V) 
        low = [float("Inf")] * (self.V) 
        parent = [-1] * (self.V) 
        if self.isBCUtil(0, visited, parent, low, disc): 
            return False
        if any(i == False for i in visited): 
            return False
          
        return True


# In[12]:


# Задание графов(матрица инцидентности)
N=-1

while N <= 0:
    N = int(input('Ведите количество вершин: '))

graph=Graph(N)

print("Хотите добавить ребра? y/n ")
agree=str(input())
while(agree=="y"):
    graph.addEdge()
    agree=str(input("Ввести еще ребро? y/n "))
print ("Yes" if g2.isBC() else "No")   


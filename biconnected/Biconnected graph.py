#!/usr/bin/env python
# coding: utf-8

# In[45]:


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
        
    def addEdgeByIndex(self, u, v):
        self.graph[u].append(v) 
        self.graph[v].append(u)
        
    def removeEdge(self, u, v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)
        
    def DFS(self, fromV, toV):
        stack = [fromV]
        visited = [False] * self.V
        
        visited[fromV] = True
        
        while stack:
            vertex = stack.pop()
            
            if vertex == toV:
                return True
            
            for i in self.graph[vertex]:
                if not visited[i]:
                    stack.append(i)
                    visited[i] = True
        
        return False

    
    def makeBiconnected(self):
        counter = 0
        
        for parent in range(self.V):
            for child in self.graph[parent]:
                self.removeEdge(parent, child)
                
                if self.DFS(parent, child) == False:
                    if len(self.graph[child]) == 0:
                        vert1 = self.graph[parent][0]
                        vert2 = child
                    else:
                        vert1 = self.graph[child][0]
                        vert2 = parent
                    
                    self.addEdgeByIndex(vert1, vert2)
                    self.addEdgeByIndex(parent, child)
                    
                    parent -= 1
                    counter += 1
                    break
                
                self.addEdgeByIndex(parent, child)
        
        return counter


# In[47]:


# Задание графов(матрица инцидентности)
N = int(input('Ведите количество вершин: '))

graph=Graph(N)

print("Хотите добавить ребра? y/n ")
agree=str(input())
while(agree=="y"):
    graph.addEdge()
    agree=str(input("Ввести еще ребро? y/n "))

print("Edges to add: ", graph.makeBiconnected())


# In[ ]:





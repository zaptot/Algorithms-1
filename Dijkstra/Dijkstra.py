#!/usr/bin/env python
# coding: utf-8

# In[25]:


import sys 
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                      for row in range(vertices)] 
  
    def printSolution(self, dist): 
        print ("Vertex tDistance from Source")
        for node in range(self.V): 
            print (node,"\t",dist[node] )
  
    def minDistance(self, dist, sptSet): 
        min = sys.maxsize 
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v
        return min_index 

    def dijkstra(self, src): 
        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
        for cout in range(self.V): 
            u = self.minDistance(dist, sptSet) 
            sptSet[u] = True
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                        dist[v] = dist[u] + self.graph[u][v] 
  
        self.printSolution(dist) 


# In[27]:


def addVertex(graph):
    N=len(graph)
    for i in range(N):
        graph[i].append(0)  
    N += 1
    graph.append([0]* N)
    for i in graph:
        print(*i)
        
def addEdge(graph):
    print('Введите вершины ребра: ')
    v1=(int(input()))
    v2=(int(input()))
    print ('Введите вес ребра:')
    weight=(int(input()))
    graph[v1][v2]=weight
    graph[v2][v1]=weight

def removeVertex(graph):
    k= (int(input('Какую вершину удаляем? ')))
    for i in range(N):
        for j in range (k,N-1):
            graph[i][j]=graph[i][j+1]
        graph[i].pop(N-1)
    graph.pop(k)
    for i in graph:
        print(*i)

def removeEdge(graph):
    print('Введите вершины ребра, которое будет удалено: ')
    vertex1=(int(input()))
    vertex2=(int(input()))
    graph[vertex1][vertex2]=0
    graph[vertex2][vertex1]=0
    for i in graph:
        print(*i)


# In[31]:


# Задание графов(матрица инцидентности)
N=-1

while N <= 0:
    N = int(input('Ведите количество вершин: '))

g  = Graph(N);

print("Хотите добавить вершины? y/n ")
agree=str(input())
while(agree=="y"):
    addVertex(g.graph)
    agree=str(input("Ввести еще вершину? y/n "))

print("Хотите добавить ребра? y/n ")
agree=str(input())
while(agree=="y"):
    addEdge(g.graph)
    agree=str(input("Ввести еще ребро? y/n "))

for i in g.graph:
    print(*i)

print("Хотите удалить ребра? y/n ")
agree=str(input())
while(agree=="y"):
    removeEdge(g.graph)
    agree=str(input("Удалить еще ребро? y/n "))
    
print("Хотите удалить вершины? y/n ")
agree=str(input())
while(agree=="y"):
    removeVertex(g.graph)
    N=N-1
    agree=str(input("Удалить еще вершину? y/n "))

g.dijkstra(0); 


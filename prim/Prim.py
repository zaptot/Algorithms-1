#!/usr/bin/env python
# coding: utf-8

# In[30]:


import sys
def printMST(graph, parent): 
    print ("Prim:")
    print ("Edge \tWeight")
    for i in range(1,N): 
        print (parent[i],"-",i,"\t",graph[i][parent[i]] )
        
def minKey(graph, key, mstSet): 
    min = sys.maxsize
    for v in range(N): 
        if key[v] < min and mstSet[v] == False: 
            min = key[v] 
            min_index = v 
    return min_index 

def primMST(graph): 
    key = [sys.maxsize] * N 
    parent = [None] * N
    key[0] = 0 
    mstSet = [False] * N 
    parent[0] = -1
    for cout in range(N): 
        u = minKey(graph,key, mstSet) 
        mstSet[u] = True
        for v in range(N): 
            if graph[u][v] > 0 and mstSet[v] == False and key[v] > graph[u][v]: 
                    key[v] = graph[u][v] 
                    parent[v] = u 
  
    graphP = printMST(graph,parent)
    primGraph=[[0 for _ in range(N)] for _ in range(N)]
    for i in range(1,N): 
        v1=parent[i]
        v2=i
        weight=graph[i][parent[i]]
        primGraph[v1][v2]=weight
        primGraph[v2][v1]=weight
    print("New graph by Prim's algorith:")
    for i in primGraph:
        print(*i)


# In[31]:


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
    v1=(int(input())-1)
    v2=(int(input())-1)
    print ('Введите вес ребра:')
    weight=(int(input()))
    graph[v1][v2]=weight
    graph[v2][v1]=weight

def removeVertex(graph):
    k= (int(input('Какую вершину удаляем? '))-1)
    for i in range(N):
        for j in range (k,N-1):
            graph[i][j]=graph[i][j+1]
        graph[i].pop(N-1)
    graph.pop(k)
    for i in graph:
        print(*i)

def removeEdge(graph):
    print('Введите вершины ребра, которое будет удалено: ')
    vertex1=(int(input())-1)
    vertex2=(int(input())-1)
    graph[vertex1][vertex2]=0
    graph[vertex2][vertex1]=0
    for i in graph:
        print(*i)


# In[29]:


# Задание графов(матрица инцидентности)
N=-1

while N <= 0:
    N = int(input('Ведите количество вершин: '))

graph=[[0 for _ in range(N)] for _ in range(N)]

print("Хотите добавить вершины? y/n ")
agree=str(input())
while(agree=="y"):
    addVertex(graph)
    agree=str(input("Ввести еще вершину? y/n "))

print("Хотите добавить ребра? y/n ")
agree=str(input())
while(agree=="y"):
    addEdge(graph)
    agree=str(input("Ввести еще ребро? y/n "))

for i in graph:
    print(*i)

print("Хотите удалить ребра? y/n ")
agree=str(input())
while(agree=="y"):
    removeEdge(graph)
    agree=str(input("Удалить еще ребро? y/n "))
    
print("Хотите удалить вершины? y/n ")
agree=str(input())
while(agree=="y"):
    removeVertex(graph)
    N=N-1
    agree=str(input("Удалить еще вершину? y/n "))

primMST(graph)


# In[ ]:





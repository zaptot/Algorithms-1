#!/usr/bin/env python
# coding: utf-8

# In[7]:


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
    for j in range(N): 
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
    return primGraph


# In[8]:


from math import inf, isinf

def kruskalMST(graph):
    kruskalGraph=[[0 for _ in range(N)] for _ in range(N)]
    minimalSpanningTree = []
    marks = {}
    for mark in range(len(graph)):
        marks[mark] = mark
    while len(minimalSpanningTree) < len(graph) - 1:
        minEdge = getMinEdge(graph, marks)[0]
        weight = getMinEdge(graph, marks)[1]
        minimalSpanningTree.append(minEdge)
        marks = changeMarks(marks, marks[minEdge[0]], marks[minEdge[1]])
        v1= minEdge[0]
        v2= minEdge[1]
        kruskalGraph[v1][v2]=weight
        kruskalGraph[v2][v1]=weight
    print("\nKruskal:")
    for i in range (len(minimalSpanningTree)):
        print (minimalSpanningTree[i])
    print("New graph by Kruskal's algorithm:")
    for i in kruskalGraph:
        print(*i)
    return kruskalGraph
    
def getMinEdge(graph, marks):
    minEdge = inf
    edge = ()
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            cell = graph[i][j]
            if cell > 0 and cell < minEdge:
                if marks[i] != marks[j]:
                    minEdge = graph[i][j]
                    edge = (i, j)
    list = []
    list.append(edge)
    list.append(minEdge)
    return list
    
def changeMarks(marks, oldMark, newMark):
    for key in marks:
        if marks[key] == oldMark:
            marks[key] = newMark
    return marks


# In[9]:


def union(graph):
    combine = [[0 for _ in range(N)] for _ in range(N)]
    prim = primMST(graph)
    kruskal = kruskalMST(graph)
    for i in range (N):
        for j in range (N):
            if (prim[i][j] == 0 and kruskal[i][j] == 0):
                    combine[i][j] = 0
            else:
                if (prim[i][j] != 0):
                    combine[i][j] = prim[i][j]
                if (kruskal[i][j] != 0):
                    combine[i][j] = kruskal[i][j]
    print("\nNew union graph algorithm:")
    for i in combine:
        print(*i)


# In[10]:


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


# In[11]:


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
    
union(graph)


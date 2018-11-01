#!/usr/bin/env python
# coding: utf-8

# In[21]:


from math import inf, isinf

def kruskal(graph):
    minimalSpanningTree = []
    marks = {}
    for mark in range(len(graph)):
        marks[mark] = mark
    while len(minimalSpanningTree) < len(graph) - 1:
        minEdge = getMinEdge(graph, marks)
        minimalSpanningTree.append(minEdge)
        marks = changeMarks(marks, marks[minEdge[0]], marks[minEdge[1]])
    return minimalSpanningTree

def getMinEdge(graph, marks):
    minEdge = inf
    edge = ();
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            cell = graph[i][j]
            if cell > 0 and cell < minEdge:
                if marks[i] != marks[j]:
                    minEdge = graph[i][j]
                    edge = (i, j)
    return edge

def changeMarks(marks, oldMark, newMark):
    for key in marks:
        if marks[key] == oldMark:
            marks[key] = newMark
    return marks


# In[22]:


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
    graph[v1][v2]=weight;
    graph[v2][v1]=weight;

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


# In[24]:


# Задание графов(матрица инцидентности)
N=-1

while N <= 0:
    N = int(input('Ведите количество вершин: '))
graph =[[0 for _ in range(N)] for _ in range(N)]

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

print("\n",kruskal(graph))


# In[ ]:





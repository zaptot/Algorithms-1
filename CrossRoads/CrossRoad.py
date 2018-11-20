#!/usr/bin/env python
# coding: utf-8

# In[254]:


from math import inf

def floydWarshall(graph): 
    e=[0 for _ in range(N)]
    rad=inf
    for k in range(N): 
        for i in range(N): 
            for j in range(N): 
                graph[i][j] = min(graph[i][j] , graph[i][k]+ graph[k][j] ) 
    print ("Кратчайшие дороги между каждой парой дорог" )
    for i in graph:
        print(*i)
    for i in range(N): 
        for j in range(N): 
            e[i]= max(e[i], graph[i][j])
        print("Самый дальный перекресток для", i, "дороги:", j, ", время до него:", e[i])
    for i in range(N):
        rad = min(rad, e[i])
        if (e[i] == rad):
            c = i
    print("пожарная станция может быть на перекрестке:",c)


# In[255]:


def addVertex(graph):
    N=len(graph)
    for i in range(N):
        graph[i].append(inf)
    N += 1
    graph.append([inf]* N)
    for i in range (N):
        graph[i][i]=0
    for i in graph:
        print(*i)
        
def addEdge(graph):
    print('Введите вершины ребра: ')
    v1=(int(input())-1)
    v2=(int(input())-1)
    print ('Введите вес:')
    weight=(int(input()))
    graph[v1][v2]=weight;


# In[256]:


# Задание графов(матрица инцидентности)
N=-1

while N <= 0:
    N = int(input('Ведите количество вершин: '))
graph =[[inf for _ in range(N)] for _ in range(N)]
for i in range(N):
    graph[i][i] = 0

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

floydWarshall(graph)


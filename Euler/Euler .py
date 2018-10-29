#!/usr/bin/env python
# coding: utf-8

# In[31]:


def findCycle(graph):
    if isEuler(graph):
        stack = []
        stack.append(0)
        res = []
        while stack:
            current = stack[-1]
            if sum(graph[current]) == 0:
                res.append(stack.pop())
            else:
                vertex = graph[current].index(1)
                graph[vertex][current] = 0
                graph[current][vertex] = 0
                stack.append(vertex)
        return res
    else:
        return None


# In[32]:


def isEuler(graph):
    for row in graph:
        if (sum(row) % 2) != 0:
            return False
    return True


# In[36]:


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
    graph[v1][v2]=1;
    graph[v2][v1]=1;


# In[37]:


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


# In[ ]:


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

print("Эйлеров: ",isEuler(graph))
print("Цикл: ",findCycle(graph))


# In[ ]:





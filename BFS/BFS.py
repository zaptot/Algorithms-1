#!/usr/bin/env python
# coding: utf-8

# In[3]:


def addEdge(graph):
    print('Введите вершины ребра: ')
    v1=(int(input()))
    v2=(int(input()))
    graph[v1][v2]=1;
    graph[v2][v1]=1;


# In[4]:


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


# In[5]:


def matrix_to_list(matrix):
    graph = {}
    for i, node in enumerate(matrix):
        adj = []
        for j, connected in enumerate(node):
            if connected:
                adj.append(j)
        graph[i] = adj
    return graph


# In[50]:


def BFS(graph, s, visited, colors): 
        # Mark all the vertices as not visited 
        queue = [] 
  
        # Mark the source node as  
        # visited and enqueue it 
        queue.append(s) 
        visited[s] = True
        colors[s]=1
        while queue: 
  
            # Dequeue a vertex from  
            # queue and print it 
            s = queue.pop(0) 
            print (s, end = " ") 
            # Get all adjacent vertices of the 
            # dequeued vertex s. If a adjacent 
            # has not been visited, then mark it 
            # visited and enqueue it 
            for i in graph[s]: 
                if visited[i] == False: 
                    colors[i]=3-colors[s]
                    queue.append(i) 
                    visited[i] = True


# In[56]:


def connectedComponents(list): 
    componentsNumber = 0
    visited = [False] * (N)
    colors=[0]*(N)
    for i in range(N):
        if visited[i]==False:
            print("Component number ",componentsNumber, ": ",end=" ")
            componentsNumber+=1
            BFS(list,i,visited,colors)


# In[57]:


def isDicotyledonous(list):
    colors=[0]*(N)
    visited = [False] * (N)
    BFS(list, 0, visited, colors)
    for i in range(N):
        for j in range(len(list[i])):
            if colors[i]==colors[list[i][j]]:
                return False
    print("\nFirst part: ")
    for i in range(N):
        if colors[i]==1:
            print(i)
    print("\nSecond part: ")
    for i in range(N):
        if colors[i]==2:
            print(i)
    return True


# In[58]:


# Задание графа (матрица инцидентности)
N=int(input('Количество вершин: '))
        
graph=[[0 for _ in range(N)] for _ in range(N)]

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
    
list=matrix_to_list(graph)
print(list)

if isDicotyledonous(list)==False:
    print("Этот граф не двудольный")
connectedComponents(list)

print("\nХотите добавить ребра? y/n ")
agree=str(input())
while(agree=="y"):
    addEdge(graph)
    agree=str(input("Ввести еще ребро? y/n "))

print("Было:")
connectedComponents(list)
list=matrix_to_list(graph)
print("\nСтало:")
connectedComponents(list)


# In[ ]:





# In[ ]:





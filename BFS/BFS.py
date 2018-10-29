#!/usr/bin/env python
# coding: utf-8

# In[4]:


def addEdge(graph):
    print('Введите вершины ребра: ')
    v1=(int(input()))
    v2=(int(input()))
    graph[v1][v2]=1;
    graph[v2][v1]=1;


# In[5]:


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


# In[6]:


def matrix_to_list(matrix):
    graph = {}
    for i, node in enumerate(matrix):
        adj = []
        for j, connected in enumerate(node):
            if connected:
                adj.append(j)
        graph[i] = adj
    return graph


# In[7]:


def BFS(graph, s): 
        # Mark all the vertices as not visited 
        visited = [False] * (len(graph)) 
  
        # Create a queue for BFS 
        queue = [] 
  
        # Mark the source node as  
        # visited and enqueue it 
        queue.append(s) 
        visited[s] = True
  
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
                    queue.append(i) 
                    visited[i] = True


# In[27]:


def connectedComponents(list): 
    def findComponents(Node,Component):
        while Node != Component[Node][0]: 
            Node = Component[Node][0] 
        return (Node,Component[Node][1]) 
    components = {} 
    for myNode in list.keys(): 
        components[myNode] = (myNode,0) 
    for i in list: 
        for j in list[i]: 
            (components_i,DepthI) = findComponents(i,components) 
            (components_j,DepthJ) = findComponents(j,components) 
            if components_i != components_j: 
                Min = components_i 
                Max = components_j
                if DepthI > DepthJ: 
                    Min = components_j 
                    Max = components_i 
                components[Max] = (Max,max(components[Min][1]+1,components[Max][1])) 
                components[Min] = (components[Max][0],-1) 
    items = {} 
    for i in list: 
        if components[i][0] == i: 
            items[i] = [] 
    for i in list: 
        items[findComponents(i,components)[0]].append(i) 
    return items 


# In[29]:


# Задание графа (матрица инцидентности)
N=int(input('число строк и столбцов: '))
        
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
m=int((input('C какой вершины начинаем? ')))
BFS(list,m) 

print("\n",connectedComponents(list))

print("Хотите добавить ребра? y/n ")
agree=str(input())
while(agree=="y"):
    addEdge(graph)
    agree=str(input("Ввести еще ребро? y/n "))

list=matrix_to_list(graph)
print("\n",connectedComponents(list))


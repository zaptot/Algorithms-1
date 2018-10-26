#!/usr/bin/env python
# coding: utf-8

# In[77]:


def findCycle(graph):
    if is_euler(graph):
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


# In[78]:


def isEuler(graph):
    for row in graph:
        if (sum(row) % 2) != 0:
            return False
    return True


# In[79]:


# Задание графов(матрица инцидентности)
withoutCycle0 = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0],
]

withCycle0 = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
]

withoutCycle = [
    [0, 1, 0, 1],
    [1, 0, 0, 0],
    [0, 0, 0, 0],
    [1, 0, 0, 0],
]

withCycle = [
    [0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0],
]


# In[80]:


print(isEuler(withCycle))
print(isEuler(withoutCycle))


# In[81]:


print(findCycle(withoutCycle0))
print(findCycle(withCycle0))
print(findCycle(withoutCycle))
print(findCycle(withCycle))


# In[ ]:





# In[ ]:





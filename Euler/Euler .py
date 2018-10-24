#!/usr/bin/env python
# coding: utf-8

# In[10]:


def find_cycle(graph):
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


def is_euler(graph):
    for row in graph:
        if (sum(row) % 2) != 0:
            return False
    return True


# In[11]:


with_cycle1 = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0],
]

with_cycle = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
]

without_cycle = [
    [0, 1, 0, 1],
    [1, 0, 0, 0],
    [0, 0, 0, 0],
    [1, 0, 0, 0],
]


# In[12]:


print(find_cycle(with_cycle1))
print(find_cycle(with_cycle))
print(find_cycle(without_cycle))


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[16]:


from collections import deque

def isGraphClosed(graph):
    itemsToSearch = deque()

    firstKey = next(iter(graph.keys()))
    itemsToSearch += graph[firstKey]

    searched = set()
    searched.add(firstKey)
    while itemsToSearch:
        current = itemsToSearch.popleft()
        if current not in searched:
            searched.add(current)
            itemsToSearch += graph[current]

    return len(searched) == len(graph)


# In[17]:


closedGraph = {
    0: [1, 3],
    1: [0, 4],
    2: [3],
    3: [0, 2, 4],
    4: [1, 3],
}

unclosedGraph = {
    0: [1, 3],
    1: [0, 4],
    2: [],
    3: [0, 4],
    4: [1, 3],
}


# In[18]:


print(isGraphClosed(closedGraph))
print(isGraphClosed(unclosedGraph))


# In[ ]:





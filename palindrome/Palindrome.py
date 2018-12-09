#!/usr/bin/env python
# coding: utf-8

# In[45]:


def createLength(string):
    length=[[0 for _ in range(len(string))] for _ in range(len(string))]
    for i in range (len(string)):
        for j in range (len(string)):
            if i == j:
                length[i][j]=1
            else:
                if i<j:
                    length[i][j]=-1
                else:
                    length[i][j]=0
    return length

def findLength(left, right, string):
    length = createLength(string)
    if length[left][right] == -1:
        if string[left] == string[right]:
            length[left][right] = findLength(left + 1, right - 1, string) + 2
        else :
            length[left][right] = max(findLength(left + 1, right, string), findLength(left, right - 1, string))  
    return length[left][right]


# In[46]:


string = (str(input('Your string:')))
length = len(string)-1
findLength(0,length, string)


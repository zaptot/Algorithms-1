#!/usr/bin/env python
# coding: utf-8

# In[141]:


from random import randint
import math
import random

HASH_CONSTANT = 211
PRIME = 1279
M=1000
A=(math.sqrt(5)-1)/2
A1=0.52354
A2=0.72474487
A3=0.366025

def hash_function(value):
    return math.floor(((value % HASH_CONSTANT)*A)%1*M)

def makeArray():
    return [random.randint(0, 1000) for j in range(1000)]


# In[142]:


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.last = self
        self.count = 0
    
    def add(self, value):
        if self.value == None:
            self.value = value
            self.count = 1
        else:
            node = self.last     
            
            newNode = Node(value)
            node.next = newNode 
            self.last = newNode
            self.count += 1


# In[143]:


class HashTableChain:
    values = []
    
    def __init__(self):
        self.values = [Node(None) for _ in range(M)]
    
    def add(self, number):
        key = hash_function(number)
        
        self.values[key].add(number)   
    
    def findLongestChain(self):
        longest = -1
        for i in range(len(self.values)):
            if self.values[i].count > longest: 
                longest = self.values[i].count
        
        return longest

    def __str__(self):
        for i in range(len(self.values)):
            node = self.values[i]
            
            print("\n", i, ":", end="")
            while node!=None:
                print(node.value, end=">")
                node = node.next
        
                


# In[144]:


arrA = [(math.sqrt(5)-1)/2, A1, A2, A3]

for k in range(len(arrA)):
    A = arrA[k]
    
    longest = -1

    for i in range(50):
        hashTable = HashTableChain()
        array = makeArray()

        for j in range(len(array)):
            hashTable.add(array[j])

        if hashTable.findLongestChain() > longest:
            longest = hashTable.findLongestChain()

    print(longest, "for A =", A)


# In[145]:


class OpenAddressing():

    def __init__(self, size):
        self.values = [None] * (M+24)
        
    def 


# In[138]:





# In[140]:





# In[ ]:





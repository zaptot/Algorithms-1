#!/usr/bin/env python
# coding: utf-8

# In[11]:


from random import randint
import math
import random

HASH_CONSTANT = 211
M=1000
A=(math.sqrt(5)-1)/2
A1=0.52354
A2=0.72474487
A3=1/math.sqrt(2)

def hash_function(value):
    return math.floor(((value % HASH_CONSTANT)*A)%1*M)

def makeArray():
    return [random.randint(0, 1000) for j in range(1000)]


# In[12]:


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
            node = self
            
            while node.value != value and node != self.last:
                node = node.next
            
            if node.value == value:
                return
            
            node = self.last
            newNode = Node(value)
            node.next = newNode 
            self.last = newNode
            self.count += 1


# In[13]:


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

    def find(self, number):
        node =  self.values[hash_function(number)]

        if node.value == None:
            return None

        while node.value != number:
            node = node.next

            if node == None:
                return None

        return hash_function(number)

    def printHashTable(self):
        for i in range(len(self.values)):
            node = self.values[i]
            
            print("\n", i, ":", end="")
            while node!=None:
                print(node.value, end=">")
                node = node.next
                


# In[14]:


arrA = [(math.sqrt(5)-1)/2, A1, A2, A3]

for k in range(len(arrA)):
    A = arrA[k]
    
    longest = -1

    for i in range(50):
        hashTable = HashTableChain()
        array = makeArray()

        for j in range(len(array)):
            hashTable.add(array[j])
    
#     Uncomment to show hash table
#         if i == 1 and k == 0:
#             hashTable.printHashTable()
            
        if hashTable.findLongestChain() > longest:
             longest = hashTable.findLongestChain()

    print(longest, "for A =", A)


# In[25]:


# find 

# def add

hashTable = HashTableChain()
array = makeArray()

for j in range(len(array)):
    hashTable.add(array[j])

# As if array is made by makeArray function, number 2 may either present in that array or not
# But in any case it will be saved on the same position (index) because of the same hash_function
index = hashTable.find(2)

print(index)


# In[16]:


A = (math.sqrt(5)-1)/2

def hashFunction(value):
    return math.floor(((value % HASH_CONSTANT) * A)%1 * M)

class OpenAdressing():
    values = []
    
    def __init__(self):
#         Here we don't need any linked lists
        self.values = [None for _ in range(M)]
        
    def add(self, value):
        key = hashFunction(value)
        i = 1

        if self.values[key] == None:
            self.values[key] = value
        elif self.values[key] != value:
            newKey = (key + i) % M

            while self.values[newKey] != None and self.values[newKey] != value: 
                newKey = (key + i*i) % M
                i += 1

            if self.values[newKey] != value:
                self.values[newKey] = value

        return i-1

    def find(self, value):
        key = hashFunction(value)
        i = 1

        if self.values[key] == None:
            return None
        elif self.values[key] != value:
            newKey = (key + i) % M

            while self.values[newKey] != None and self.values[newKey] != value: 
                newKey = (key + i*i) % M
                i += 1

            if self.values[newKey] == value:
                return newKey
            else:
                return None
        else:
            return key

    def printHashTable(self):
        for i in range(len(self.values)):
            print(i, ":", self.values[i])


# In[17]:


MaxI = -1

for i in range(50):
    hashTable = OpenAdressing()

    array = makeArray()
    maxI = -1

    for j in range(len(array)):
        curI = hashTable.add(array[j])

        if curI > maxI:
            maxI = curI

        if maxI > MaxI:
            MaxI = maxI
        
#     Uncomment to show table
    if i == 0:
        hashTable.printHashTable()
print(MaxI)  


# In[18]:


hashTable = OpenAdressing()
array = makeArray()

for j in range(len(array)):
    hashTable.add(array[j])

print(hashTable.find(6))


# In[19]:


hashTable.printHashTable()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[101]:


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


# In[102]:


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


# In[120]:


class HashTableChain:
    values = []
    
    def __init__(self):
        self.values = [Node(None) for _ in range(M)]
    
    def add(self, number):
        key = hash_function(number)
        
        self.values[key].add(number)   
        
    def remove(self, number):
        key = hash_function(number)
        if key in self.values.keys() and number in self.values[key]:
            self.values[key].pop(self.values[key].index(number))
            if not len(self.values[key]):
                self.values.pop(key)
        else:
            raise ValueError('Item is not exist.')

    def find(self, number):
        key = hash_function(number)
        if number in self.values and number != None:
            return self.values[key][self.values[key].index(number)]
        else:
            raise ValueError('Could not find value.')
    
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
        
                


# In[121]:


arrA = [(math.sqrt(5)-1)/2, A1, A2, A3]

for k in range(len(arrA)):
    A = arrA[k]
    
    longest = -1

    for i in range(50):
        hashTable = HashTableChain()
        array = makeArray()

        for j in range(len(array)):
            hashTable.add(array[j])
        hashTable.add(350)
        hashTable.find(350)
#         hashTable.remove(350)
#         print(hashTable)

        if hashTable.findLongestChain() > longest:
            longest = hashTable.findLongestChain()

    print(longest, "for A =", A)



# In[ ]:


# class OpenAddressing():

#     def __init__(self, size):
#         self._size = 0
#         self._max_size = size
#         data_len = 0
#         while size > 0:
#             size >>= 1
#             data_len += 1
#         self.data = [None] * (2**data_len)

#     def get(self, key):
#         hashh = self.hash(key)
#         ind = hashh
#         trry = 0
#         while self.data[ind] is not None and self.data[ind][0] != key:
#             trry += 1
#             ind = (hashh + (trry ** 2)) % len(self.data)
#         return None if self.data[ind] is None else self.data[ind][1]

#     def set(self, key, value):
#         if self._size == self._max_size:
#             for index, val in enumerate(self.data):
#                 if val is not None and val[0] == key:
#                     self.data[index][1] = value
#                     break
#             else:
#                 raise Exception('Cannot insert new element into a full hash table')

#         hashh = self.hash(key)
#         ind = hashh
#         trry = 0
#         while self.data[ind] is not None:
#             if self.data[ind][0] != key:
#                 trry += 1
#                 ind = (hashh + (trry ** 2)) % len(self.data)
#             else:
#                 self.data[ind][1] = value
#                 return trry
#         self.data[ind] = [key, value]
#         self._size += 1
#         return trry

#     def hash(self, key):
#         return math.floor(key * OpenAddressingHashTable.PRIME) % len(self.data)


#     for arr in h:
#         htable = OpenAddressingHashTable(len(arr))

#     for k, v in enumerate(arr):
#         tries = htable.set(k, v)
#         worst = tries if tries > worst else worst

#     print("Max tries during insertion with serial keys:", worst)

#     worst = 0

#     for arr in h:
#         htable = OpenAddressingHashTable(len(arr))

#         for v in arr:
#             tries = htable.set(random.randint(0, 1024), v)
#             worst = tries if tries > worst else worst

#     print("Max tries during insertion with random keys:", worst)


# In[ ]:





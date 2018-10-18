#!/usr/bin/env python
# coding: utf-8

# In[63]:


import json
from random import randint
import math

HASH_CONSTANT = 211
M=1000
A=(math.sqrt(5)-1)/2
A1=0.52354
A2=0.72474487
A3=0.366025

def hash_function(value):
    return (value % HASH_CONSTANT)*A*M


class HashTable:
    values = {}
    
    def add(self, number):
        self.next = None
        self.last = self
        key = hash_function(number)
        if key in self.values.keys():
            if number not in self.values[key]:
                self.values[key].append(number)
        else:
            self.values[key] = [number]
            
    def __str__(self):
        keys = sorted(self.values.keys())
        a=max(json.dumps(len(self.values[key]))for key in keys)
        return a
#         return ''.join([str(key) + ': ' + json.dumps(self.values[key])+json.dumps(len(self.values[key]))+'\n'+a for key in keys])
        
        
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
        if key in self.values.keys() and number in self.values[key]:
            return self.values[key][self.values[key].index(number)]
        else:
            raise ValueError('Could not find value.')



if __name__ == '__main__':
    hashTable = []
    for j in range (1,50):
        print(j, 'HashTable')
        h=HashTable()
        hashTable.append(h)
        
        for i in range(M):
            k=randint(0,M)
            h.add(k)
        print(h,'\n')
        
#         hashTable.add(350)
#         print(hashTable.find(350))
#         hashTable.remove(350)

#         try:
#             print(hashTable.find(350))
#         except ValueError:
#             print('Could not find value.')


# In[4]:





# In[ ]:





# In[ ]:





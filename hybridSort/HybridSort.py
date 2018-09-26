#!/usr/bin/env python
# coding: utf-8

# In[20]:


import random
import sys
import timeit
import time 

#creation
ARRAY_LENGTH = 10 ** 5
NUMBER_TO = 10 ** 9
k=200

def writeInFile():
    for file in range(50):
        f = open("array{}.txt".format(file), "w+")
    
        for i in range(ARRAY_LENGTH):
            f.write("{}".format((int)(random.random() * (NUMBER_TO+1))) + "\n")
        f.close()
    
    
def readFiles(index):
    f = open("array{}.txt".format(index), "r")
    arr = []
    
    for line in f:
        arr.append(int(line))
    
    return arr



# hybrid sort
def hybridSort(arr, first, last):
    if first < last:
        if (last-first) > k:
            middle = (first+last)//2            
            hybridSort(arr, first, middle)
            hybridSort(arr, middle+1, last)
            merge(arr, first, middle, last)
        else:
            insertionSort(arr, first, last + 1) 

# merge sort
def mergeSort(arr, first, last):
    if first < last:
            middle = (first+last)//2            
            mergeSort(arr, first, middle)
            mergeSort(arr, middle+1, last)
            merge(arr, first, middle, last)

def merge(arr, first, middle, last):
    left = arr[first:middle+1]
    right = arr[middle+1:last+1]
    left.append(sys.maxsize)
    right.append(sys.maxsize)
    i = j = 0

    for k in range (first, last+1):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

# insertion sort
def insertionSort(arr, first, last):
    for i in range(first + 1, last-first):
        curr = arr[i]
        j = i-1
        while arr[j] > arr[j+1] and j >= first:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                j -= 1
        arr[j+1] = curr


# In[21]:


writeInFile()


# In[ ]:


t3 = time.time()
for n in range(50):
    a = readFiles(n)
    mergeSort(a, 0, len(a)-1)
t4=time.time()-t3
while k < 201:
    t = time.time()
    for n in range(50):
        a = readFiles(n)
        hybridSort(a, 0, len(a)-1)
    t2=time.time()-t
    if(t2 < t4):
        print(t4-t2,k)
    k -= 1
# insertionSort(a, 0, len(a))
#print (a)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





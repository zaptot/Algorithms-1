#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

# merge sort
def mergeSort(arr, first, last):
    if first < last:
        if (last-first) > k:
            middle = (first+last)//2            
            mergeSort(arr, first, middle)
            mergeSort(arr, middle+1, last)
            merge(arr, first, middle, last)
        else:
            insertionSort(arr, first, last + 1) 

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

# 2 megre            
# def merge1(arr, first, middle, last):
#     m=0
#     k=0
#     result = [None] *(last-first)
#     while ((first + m) < middle and (middle + k) < last):
#         if a[first + m] < a[middle + k]:
#             result[m + k] = a[first + m]
#             m += 1
#         else:
#             result[m + k] = a[middle + k]
#             k += 1
  
#     while (first + m) < middle:
#         result[m + k] = a[first + m]
#         m += 1
  
#     while middle + k < last:
#         result[m + k] = a[middle + k]
#         k += 1
  
#     for i in range(m + k):
#         a[first + i] = result[i]


# insertion sort
def insertionSort(arr, first, last):
    for i in range(first + 1, last-first):
        curr = arr[i]
        j = i-1
        while arr[j] > arr[j+1] and j >= first:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                j -= 1
        arr[j+1] = curr


# In[2]:


# writeInFile()


# In[3]:


# t = time.time()
# while k <201:
#     t=time.time()
for n in range(50):
    a = readFiles(n)
    mergeSort(a, 0, len(a)-1)
#     print(k)
#     k -= 1
#     t2=(time.time()-t)
#     print(t2)
# print(time.time() - t)
# insertionSort(a, 0, len(a))
#print (a)

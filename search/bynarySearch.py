#!/usr/bin/env python
# coding: utf-8

# In[15]:


import time

NUM_TO_FIND = 6

# arr - sorted array
def binarySearch(arr, item):
    first = 0
    last = len(arr) - 1
    result = dict.fromkeys(['iteration', 'index'])
    result['iteration'] = 0
    result['index'] = -1
    while first <= last:
        result['iteration'] += 1
        middle = (last + first) // 2
        current = arr[middle]
        if current == item:
            result['index'] = middle
            return result
        if item < current:
            last = middle - 1
        if item > current:
            first = middle + 1
    return result

def interpolationSearch(arr, item):
    first = 0
    last = len(arr) - 1
    result = dict.fromkeys(['iteration', 'index'])
    result['iteration'] = 0
    result['index'] = -1
    while (first <= last and
            arr[first] <= item <= arr[last]):
        result['iteration'] += 1
        middle = first + ((item - arr[first]) * (last - first))// (arr[last] - arr[first])
        current = arr[middle]
        if current == item:
            result['index'] = middle
            return result
        if item < current:
            max_index = middle - 1
        if item > current:
            first = middle + 1
    return result

def quickSort(arr, first, last):
    if first < last:
        q = findQ(arr, first, last)
        quickSort(arr, first, q-1)
        quickSort(arr, q+1, last)    
    return arr;

def findQ(arr, first, last):
    pivot = arr[last]
    index_of_smaller = first - 1
    for j in range(first,last):
        if (arr[j] <= pivot):
            index_of_smaller += 1
            temp = arr[index_of_smaller]
            arr[index_of_smaller] = arr[j]
            arr[j] = temp
    temp = arr[index_of_smaller + 1]
    arr[index_of_smaller + 1] = arr[last]
    arr[last] = temp

    return (index_of_smaller + 1);   


# In[16]:


a=[1,2,31,4,5,16,7,8,9,56,554,245,234,14,3,6,22,11,26,17,13]
quickSort(a,0,len(a)-1)

# print(binarySearch(a, NUM_TO_FIND))
# print(interpolationSearch(a, NUM_TO_FIND))

# Binary search time executing.
binTime = time.time()
binarySearch(a, NUM_TO_FIND)
binTime = time.time() - binTime

# Interpolation search time executing.
interTime = time.time()
interIndex = interpolationSearch(a, NUM_TO_FIND)
interTime = time.time() - interTime

# print(a)
print('Binary search time:', binTime)
print('Interpolation search time:', interTime)
print('Interpolation search faster:', binTime - interTime)


# In[2]:





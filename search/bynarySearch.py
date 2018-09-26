#!/usr/bin/env python
# coding: utf-8

# In[35]:


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


# In[36]:


a=[1,2,31,4,5,16,7,8,9,56,554,245,234,14,3,6,22,11,26,17,13]
a.sort()

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





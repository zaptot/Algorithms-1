#!/usr/bin/env python
# coding: utf-8

# In[1]:


def quickSort(arr, first, last):
    if first < last:
        q = findQ(arr, first, last)
        quickSort(arr, first, q-1)
        quickSort(arr, q+1, last)    
    return arr;

def findQ(arr, first, last):
    pivotvalue = arr[first]
    left = first+1
    right = last
    done = False
    while not done:
        while left <= right and arr[left] <= pivotvalue:
            left = left + 1
        while arr[right] >= pivotvalue and right >= left:
            right = right -1
        if right < left:
            done = True
        else:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
    temp = arr[first]
    arr[first] = arr[right]
    arr[right] = temp
    return right
        


# In[2]:


people = [[27,'Jim'], [32,'Pam'], [25,'Micheal'], [44,'Dwight']]
salary = [['Jim','500$'], ['Pam','200$'], ['Micheal','150$'], ['Dwight','100$']]
quickSort(people,0,len(people)-1)
print('First sorted massive:')
print(people)
print('Second sorted massive:')
for n in range(len(people)):
    p=people[n]
    ind=p[1]
    for i in range(len(salary)):
        s=salary[i]
        ind2=s[0]
        if ind == ind2:
            s2=[]
            s2 = salary[i]
    print(s2)


# In[ ]:





# In[ ]:





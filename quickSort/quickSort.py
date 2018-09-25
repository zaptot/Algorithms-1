#!/usr/bin/env python
# coding: utf-8

# In[39]:


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


# In[40]:


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





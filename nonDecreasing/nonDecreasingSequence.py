#!/usr/bin/env python
# coding: utf-8

# In[111]:


def subsequence(seq):
    M = [None] * len(seq)
    P = [None] * len(seq)
    result = []
    L = 1
    M[0] = 0
    for i in range(1, len(seq)):
        lower = 0
        upper = L
        if seq[M[upper-1]] < seq[i]:
            j = upper
        else:
            while upper - lower > 1:
                mid = (upper + lower) // 2
                if seq[M[mid-1]] < seq[i]:
                    lower = mid
                else:
                    upper = mid
            j = lower
        P[i] = M[j-1]
        if j == L or seq[i] < seq[M[j]]:
            M[j] = i
            L = max(L, j+1)
    pos = M[L-1]
    for _ in range(L):
        result.append(seq[pos])
        pos = P[pos]

    return result[::-1] 


# In[112]:


N = (int(input('Count of elements in sequence:')))
seq=[0 for _ in range(N)]
for i in range (N):
    x = int(input('Element of sequence:'))
    seq[i]=x
subsequence(seq)


# In[ ]:





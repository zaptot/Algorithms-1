#!/usr/bin/env python
# coding: utf-8

# In[41]:


def initial(n,m, dp):
    for i in range (n):
        for j in range (m):
            dp[i][j] = -1
    dp[0][0] = 1
    return dp

def solve(i, j, dp, n, m):
    initial(i, j, dp)
    if ((i >= 0) and (j >= 0) and (i < n) and (j < m)):
        if dp[i][j] == -1:     
            dp[i][j] = solve(i - 2, j - 1, dp, n, m) + solve(i - 2, j + 1, dp, n, m) + solve(i - 1, j - 2, dp, n, m) + solve(i + 1, j - 2, dp, n, m)
        else:
            return 0
    return dp[i][j]


# In[42]:


n=(int(input('Введи n:')))
m=(int(input('Введи m:')))
dp=[[0 for _ in range(n)] for _ in range(m)]
solve(n - 1, m - 1, dp, n, m)


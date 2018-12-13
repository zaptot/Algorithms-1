#!/usr/bin/env python
# coding: utf-8

# In[22]:


def initial(n,m):
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    dp[0][0] = 1
    return dp

def solve(i, j, dp, n, m):
    if i >= 0 and j >= 0 and i < n and j < m:
        if dp[i][j] == -1:     
            dp[i][j] = solve(i - 2, j - 1, dp, n, m) + solve(i - 2, j + 1, dp, n, m) + solve(i - 1, j - 2, dp, n, m) + solve(i + 1, j - 2, dp, n, m)
    else:
        return 0
    return dp[i][j]


# In[24]:


n=(int(input('Введи n:')))
m=(int(input('Введи m:')))

dp=initial(n,m)
print(solve(n - 1, m - 1, dp, n, m))


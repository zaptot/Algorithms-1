#!/usr/bin/env python
# coding: utf-8

# In[21]:


refuse = 0
suggest = 1
accept = 2

def work(men, job):
    worked = [[refuse for _ in job] for _ in men]
    pairs = []
    pairsNumber = len(men);
    unapairedManIndex = getUnworkedMan(worked)
    while unapairedManIndex is not None:
        prefJobIndex = men[unapairedManIndex].pop(0)

        while unapairedManIndex not in job[prefJobIndex]:
            prefJobIndex = men[unapairedManIndex].pop(0)

        manIndex = job[prefJobIndex].index(unapairedManIndex)
        worked = deletePrevSuggestion(worked, prefJobIndex)

        if manIndex is 0:
            worked[unapairedManIndex][prefJobIndex] = accept
            pairs.append((unapairedManIndex, prefJobIndex))
            men = removeJobFromMen(men, prefJobIndex)
        else:
            worked[unapairedManIndex][prefJobIndex] = suggest

        job[prefJobIndex] = job[prefJobIndex][:manIndex]
        unapairedManIndex = getUnworkedMan(worked)
    return pairs

def getUnworkedMan(worked):
    unworked = None
    for manIndex in range(len(worked)):
        if suggest not in worked[manIndex] and accept not in worked[manIndex]:
            return manIndex
        if accept not in worked[manIndex] and unworked is None:
            unworked = manIndex
    return unworked

def removeJobFromMen(men, job):
    for man in men:
        try:
            man.remove(job)
        except ValueError:
            pass
    return men

def deletePrevSuggestion(worked, job):
    for man in worked:
        if man[job] is accept or man[job] is suggest:
            worked[worked.index(man)][job] = refuse
            return worked
    return worked


# In[24]:


men = [[0, 1, 2], [2, 0, 1], [2, 1, 0]]

job = [[2, 1, 0], [1, 0, 2], [0, 2, 1]]

print(work(men, job))


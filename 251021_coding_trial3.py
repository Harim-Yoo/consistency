nums = list(range(1,16))
res = []

def dfs(start,path):
    if len(path) == 3:
        if (path[0]%3+path[1]%3+path[2]%3)==5:
            res.append(path.copy())
        return None
    for i in range(start,len(nums)):
        path.append(nums[i])
        dfs(i+1,path)
        path.pop()

dfs(0,[])
print(res)
print(len(res))
    
---------------------------------------------------------------

import math 

nums = list(range(1,13))
res = []

def dfs(start,path):
    if len(path) == 4:
        if sum(path)==24:
            if math.prod(path)%2==0:
                res.append(path.copy())
        return None
    for i in range(start,len(nums)):
        path.append(nums[i])
        dfs(i+1,path)
        path.pop()

dfs(0,[])
print(res)
print(len(res))

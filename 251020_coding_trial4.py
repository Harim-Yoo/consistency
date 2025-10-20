nums = list(range(21))

res = []

def dfs(start,path):
    if len(path)==3:
        if sum(path)<=30:
            res.append(path.copy())
    if sum(path)>30:
        return None
    for i in range(start,len(nums)):
        path.append(nums[i])
        dfs(i+1,path)
        path.pop()
    
dfs(0,[])

print(res)

------------------------------------------------

import math 
nums = list(range(-5,6))

res = []

def dfs(start,path):
    if len(path)==3:
        if math.prod(path)<0:
            res.append(path.copy())
        return None
    for i in range(start,len(nums)):
        path.append(nums[i])
        dfs(i+1,path)
        path.pop()
    
dfs(0,[])

print(res)

------------------------------------------------

nums = list(range(10))
res = []
def dfs(start,path):
    if len(path)==4:
        if sum(path)==15:
            res.append(path.copy())
        return None
    for i in range(start,len(nums)):
        path.append(nums[i])
        dfs(i+1,path)
        path.pop()

dfs(0,[])
print(res)

------------------------------------------------

import math 

nums = list(range(1,16))

res = []
def dfs(start,path):
    if len(path)==4:
        v = math.isqrt(math.prod(path))
        if v*v == math.prod(path):
            res.append(path.copy())
        return None
    for i in range(start,len(nums)):
        path.append(nums[i])
        dfs(i+1,path)
        path.pop()

dfs(0,[])
print(res)

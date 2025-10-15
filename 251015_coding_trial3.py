nums = list(range(1,7))

def perm(nums):
    res = []
    def dfs(path):
        if len(path)==len(nums):
            res.append(path.copy())
            return None
        for i in range(len(nums)):
            if nums[i] not in path:
                path.append(nums[i])
                dfs(path)
                path.pop()
    dfs([])
    return res

ans = []

for vals in perm(nums):
    if all([(vals[i]-vals[i-1])%2!=0 for i in range(1,len(vals))]):
        ans.append(vals)

print(ans)

-------------------------------------------------------------------------------------------------

import math
nums = list(range(1,7))

def perm(nums):
    res = []
    def dfs(path):
        if len(path)==len(nums):
            res.append(path.copy())
            return None
        for i in range(len(nums)):
            if nums[i] not in path:
                path.append(nums[i])
                dfs(path)
                path.pop()
    dfs([])
    return res

ans = []

for vals in perm(nums):
    if all([math.gcd(vals[i],vals[i-1])==1 for i in range(1,len(vals))]):
        ans.append(vals)

print(ans)

-----------------------------------------------------------------------------------------------

import math
nums = list(range(1,8))

def perm(nums):
    res = []
    def dfs(path):
        if len(path)==len(nums):
            res.append(path.copy())
            return None
        for i in range(len(nums)):
            if nums[i] not in path:
                path.append(nums[i])
                dfs(path)
                path.pop()
    dfs([])
    return res

ans = []

for vals in perm(nums):
    if all([(vals[i]+vals[i-1]+vals[i-2])%2==0 for i in range(2,len(vals))]):
        ans.append(vals)

print(len(ans))

----------------------------------------------------------------------------------------------


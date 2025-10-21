nums = list(range(-5,11))
import math 
res = []


def dfs(start, path):
    if len(path)==3:
        if math.prod(path)<=50:
            res.append(path.copy())
        return None
    for i in range(start,len(nums)):
        path.append(nums[i])
        dfs(i+1,path)
        path.pop()

dfs(0,[])
print(res)

import math 

nums = list(range(1,13))
res = []

def dfs(start,path):
    parity = 0
    if len(path)==4:
        for i in range(len(path)):
            if path[i]%2==0:
                parity +=1
        if parity == 2 and sum(path)==20:
            res.append(path.copy())
        return None
    for i in range(start,len(nums)):
        path.append(nums[i])
        dfs(i+1,path)
        path.pop()

dfs(0,[])
print(res)

nums = list(range(10))

res = []

def dfs(start,path):
    if len(path)==3:
        if sum(path)==10:
            res.append(path.copy())
        return None
    for i in range(start,len(nums)):
        if nums[i] not in path:
            path.append(nums[i])
            dfs(i+1,path)
            path.pop()
    
dfs(0,[])
print(res)

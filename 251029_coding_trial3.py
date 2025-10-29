nums = list(range(1,11))
res = []
 
def dfs(path):
    if len(path)==3:
        if sum(path)%3==0:
            res.append(path.copy())
        return None 
    for i in range(len(nums)):
        path.append(nums[i])
        dfs(path)
        path.pop()
dfs([])
print(len(res))

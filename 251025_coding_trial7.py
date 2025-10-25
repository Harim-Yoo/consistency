nums = list(range(1,10))
res = []

def dfs(path):
    if len(path)==len(nums):
        if all(path[i]<path[i+1] for i in range(0,4)) and all(path[i]<path[i+1] for i in range(5,8)):
            res.append(path.copy())
        return None
    for i in range(len(nums)):
        if nums[i] not in path:
            path.append(nums[i])
            dfs(path)
            path.pop()
dfs([])
print(len(res))

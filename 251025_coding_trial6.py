nums = [1,3,5,7,9,11,13,15,19]
res = []

def dfs(path):
    if len(path)==3:
        if sum(path)==19:
            res.append(path.copy())
        return None 
    for i in range(len(nums)):
        path.append(nums[i])
        dfs(path)
        path.pop()
dfs([])
print(len(res))

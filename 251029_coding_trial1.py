nums = list(range(1,101))
res = []

def dfs(layer,path):
    if layer == 3:
        if sum(path[i] for i in [0,1,2])==100:
            res.append(path.copy())
        return None 
    if layer == 0:
        for i in range(len(nums)):
            path.append(nums[i])
            dfs(layer+1,path)
            path.pop()
    elif layer == 1:
        a = path[0]
        for i in range(len(nums)):
            if nums[i] % a == 0:
                path.append(nums[i])
                dfs(layer+1,path)
                path.pop()
    else:
        a = path[0]
        for i in range(len(nums)):
            if nums[i] % a == 0:
                path.append(nums[i])
                dfs(layer+1,path)
                path.pop()
dfs(0,[])
print(len(res))

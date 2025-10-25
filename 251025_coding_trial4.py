nums = ['A','A','A','B','C','D','E']
res = []
used = [False]*len(nums)

def dfs(path):
    if len(path)==3:
        res.append(path.copy())
        return None 
    for i in range(0,len(nums)):
        if used[i] == True:
            continue
        if i>0 and nums[i] == nums[i-1] and not used[i-1]:
            continue
        used[i] = True
        path.append(nums[i])
        dfs(path)
        path.pop()
        used[i] = False
dfs([])

print(len(res))

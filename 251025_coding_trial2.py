nums = [1,2,3,4,5,6,7,8,9]
res = []

def dfs(start,path):
    if len(path)==3:
        if all(path[i]<path[i+1] for i in range(0,len(path)-1)):
            res.append(path.copy())
        return None
    for i in range(start,len(nums)):
        path.append(nums[i])
        dfs(i+1,path)
        path.pop()
    
dfs(0,[])
print(res[69])

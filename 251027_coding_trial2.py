nums = [1,2,3,4,5,6]
res = []

def dfs(start,path):
    if len(path) == 4:
        res.append(path.copy())
        return None 
    for i in range(start,len(nums)):
        path.append(nums[i])
        dfs(i+1,path)
        path.pop()

dfs(0,[])
print(res)

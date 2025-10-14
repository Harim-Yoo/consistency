nums = [1,2,3,4]

def combinations(nums):
    res = []
    
    def dfs(start,path):
        if len(path)==2:
            res.append(path.copy())
        for i in range(start,len(nums)):
            path.append(nums[i])
            dfs(i+1,path)
            path.pop()
    
    dfs(0,[])
    return res

print(combinations(nums))

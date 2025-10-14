nums = list(range(1,10))

def comb(nums):
    res = []
    
    def dfs(start,path):
        if len(path)==0:
            res.append([])
        for i in range(start,len(nums)):
            path.append(nums[i])
            res.append(path.copy())
            dfs(i+1,path)
            path.pop()
    dfs(0,[])
    
    return res
    
ans = []
for val in comb(nums):
    if sum(val)==10 and all(val[i+1]-val[i]>1 for i in range(len(val)-1)):
        ans.append(val)
        
print(ans)

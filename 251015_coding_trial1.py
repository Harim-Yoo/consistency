nums = list(range(11))

def subset(nums):
    res=[]
    res.append([])
    def dfs(start,path):
        for i in range(start,len(nums)):
            if nums[i] not in path:
                path.append(nums[i])
                if len(path)==4:
                    res.append(path.copy())
                dfs(i+1,path)
                path.pop()
    dfs(0,[])
    return res

ans = []
diff = []
for vals in subset(nums):
    if all([vals[i]-vals[i-1]>1 for i in range(1,len(vals))]):
        diff.append(vals)
        
print(len(diff))

nums = list(range(13))

def pairing(nums):
    res = []
    def dfs(start,path):
        for i in range(start,len(nums)):
            if nums[i] not in path:
                path.append(nums[i])
                if len(path)==2:
                    res.append(path.copy())
                dfs(i+1,path)
                path.pop()
    dfs(0,[])
    return res

print(len(pairing(nums)))

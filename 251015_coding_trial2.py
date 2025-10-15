nums = list(range(11))

def comb(nums):
    res = []
    def dfs(start,path):
        for i in range(start,len(nums)):
            if nums[i] not in path:
                path.append(nums[i])
                if len(path)==5 and sum(path)%2==0 and sum([val % 2 == 1 for val in path])==2 and max(path)-max(path)<=6:
                    res.append(path.copy())
                dfs(i+1,path)
                path.pop()
    dfs(0,[])
    return res

print(len(comb(nums)))


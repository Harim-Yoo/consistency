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

-----------------------------------------------------------

from itertools import combinations
nums = [1,2,3,4,5,6]
res = []

for (a,b,c,d) in combinations(nums,r=4):
    res.append((a,b,c,d))
    
print(len(res))

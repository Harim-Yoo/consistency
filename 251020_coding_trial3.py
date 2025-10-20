nums = [3,7,9,13,20,22,25]

res = []

def dfs(start,path):
    if sum(path)<=40:
        res.append(path.copy())
    for i in range(start,len(nums)):
        path.append(nums[i])
        dfs(i+1,path)
        path.pop()
    
dfs(0,[])

sums = []
for val in res:
    sums.append(sum(val))

maximum = max(sums)

for val in res:
    if sum(val) == maximum:
        print(val)

nums = list(range(-10,11))

def triple(nums):
    res = []
    def dfs(path):
        if len(path)==3:
            res.append(path.copy())
            return None
        for val in nums:
            if val not in path:
              path.append(val)
              dfs(path)
              path.pop()
    dfs([])
    return res

result = triple(nums)
count=0
for val in result:
    if sum(val)>0:
        count+=1
print(count)

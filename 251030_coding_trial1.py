nums = ['a','b','c']
res = []

def dfs(path):
    if len(path)>=2 and path[-2:] in (['a','a'],['b','b']):
        return None
    if len(path)==7:
        res.append(path.copy())
        return None 
    for i in range(len(nums)):
        path.append(nums[i])
        dfs(path)
        path.pop()
dfs([])
print(len(res))

1.

result = []

def dfs(path):
    if len(path)==3:
        result.append(path.copy())
        return None
    for i in range(1,4):
        path.append(i)
        dfs(path)
        path.pop()
        
dfs([])

print(result)

2. 

result = []

def dfs(path):
    if len(path)==2:
        result.append(path.copy())
        return None
    for i in range(1,4):
        if i not in path:
            path.append(i)
            dfs(path)
            path.pop()
        
dfs([])

print(result)

3. 

nums = list(range(6))
result = []

def dfs(start, path):
    if len(path)==2 and sum(path)==6:
        result.append(path.copy())
        return None
    for i in range(start,len(nums)):
        if nums[i] not in path:
            path.append(nums[i])
            dfs(i+1,path)
            path.pop()
        
dfs(0,[])

print(result)

4. 

nums = list(range(10))
result = []

def dfs(start, path):
    if len(path)==3 and sum(path)==15:
        result.append(path.copy())
        return None
    for i in range(start,len(nums)):
        if nums[i] not in path:
            path.append(nums[i])
            dfs(i+1,path)
            path.pop()
        
dfs(1,[])

print(result)

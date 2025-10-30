from collections import deque 

X = [1,2,3]
Y = [4,5,6,7,8]
res = []

queue = deque()
queue.append([])

while queue:
    path = queue.popleft()
    layer = len(path)
    
    if layer == len(X):
        res.append(path)
        continue 
    for y in Y:
        if y not in path:
            queue.append(path+[y])

print(len(res))

----------------------------------------------------------------------------------------------

X = [1,2,3]
Y = [4,5,6,7,8]
res = []

def dfs(layer,path):
    if layer == len(X):
        res.append(path.copy())
        return None 
    for y in Y:
        if y not in path:
            path.append(y)
            dfs(layer+1,path)
            path.pop()
dfs(0,[])
print(len(res))
    

from collections import deque

moves = [1,3,5]
res = []
target = 12 

def bfs(start):
    queue = deque([(start,0,[start])])
    visited = set([start])
    
    while queue:
        (x,layer,path) = queue.popleft()
        
        if x == target:
            res.append(layer)
            res.append(path)
            return None
        for move in moves:
            new_x = x + move 
            if new_x not in visited:
                queue.append((new_x,layer+1,path+[new_x]))
                visited.add(new_x)
bfs(0)
print(res)

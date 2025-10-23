from collections import deque

moves = [(1,0),(0,1),(1,1)]
res = []

def bfs(start,target):
    queue = deque([(start[0],start[1],0)])
    visited = set([start])
    while queue:
        (x,y,layer) = queue.popleft()
    
        if (x,y) == target:
            res.append(layer)
            return None
            
        for (dx,dy) in moves:
            new_x = x+dx
            new_y = y+dy
            if 0<=new_x<=target[0] and 0<=new_y<=target[1] and (new_x,new_y) not in visited:
                queue.append((new_x,new_y,layer+1))
                visited.add((new_x,new_y))

bfs((0,0),(5,4))
print(res)

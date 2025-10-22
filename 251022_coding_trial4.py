from collections import deque

moves = [ (5,0), (-5,0), (4,3), (-4,3), (4,-3), 
(-4,-3), (3,4), (3,-4), (-3,4), (-3,-4), (0,5), (0,-5)
]

res = []
def bfs(start,target):
    queue = deque([(start[0],start[1],0)])
    visited = set([start])
    
    while queue:
        x, y, layer = queue.popleft()
        
        if (x,y) == target :
            res.append(layer)
            return None
        
        for (dx,dy) in moves:
            (nx,ny) = (x+dx,y+dy)
            if (nx,ny) not in visited:
                queue.append((nx,ny,layer+1))
                visited.add((nx,ny))

bfs((0,0),(1,0))
print(res)

from collections import deque

res = []

def bfs(start):
    queue = deque([(start,0)])
    visited = set([start])
    
    while queue:
        pos, layer = queue.popleft()
        
        if pos == 20:
            res.append(layer)
            return None
        
        for move in [1,3,5]:
            new_pos = pos + move 
            if new_pos <=20 and new_pos not in visited:
                queue.append((new_pos,layer+1))
                visited.add(new_pos)
bfs(0)
print(res)

from collections import deque
moves = [1,3,5]
res = []

def bfs(start, target):
    queue = deque([(start,0)])
    visited = set([start])
    
    while queue:
        (x,layer) = queue.popleft()
        
        if x == 20:
            res.append(layer)
            return None
        for move in moves:
            new_x = x + move 
            if new_x <=20 and new_x not in visited:
                queue.append((new_x,layer+1))
                visited.add(new_x)
bfs(0,20)
print(res)

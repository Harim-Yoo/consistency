from collections import deque

moves = [(1,0),(0,1),(1,1)]
count = 0

def dfs(x,y,target):
    global count
    if x>target[0] or y>target[1]:
            return None
    if (x,y)==target:
        count +=1 
        return None
    for (dx,dy) in moves:
        new_x = x+dx
        new_y = y+dy
        if new_x<=target[0] and new_y<=target[1]:
            dfs(new_x,new_y,target)

dfs(0,0,(5,4))
print(count)

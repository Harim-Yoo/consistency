moves = [(1,0),(0,1),(1,1)]
label = ['H','V','D']
res = []
target = (5,4)
count = 0

def dfs(x,y,prev,path):
    global count
    if (x,y) == target and all(path.count(label[i])>=1 for i in range(len(label))):
        res.append(path.copy())
        count+=1
        return None
    for i, (dx,dy) in enumerate(moves):
        new_x = x+dx
        new_y = y+dy
        if 0<=new_x<=target[0] and 0<=new_y<=target[1]:
            if not (prev == 'D' and label[i] == 'D'):
                path.append(label[i])
                dfs(new_x,new_y,label[i],path)
                path.pop()

dfs(0,0,[],[])
print(res)
print(count)

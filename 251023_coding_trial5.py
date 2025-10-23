adj = {
    1:[2,6],
    2:[1,3],
    3:[2,4],
    4:[3,5],
    5:[4,6],
    6:[1,5]
}

colors = ['R','G','B','Y']
count = 0
res = [] 
def dfs(node,coloring):
    global count
    if node>6:
        count +=1
        res.append(coloring.copy())
        return None
    
            
    for c in colors:
        can_use = True
        for neighbor in adj[node]:
            if neighbor in coloring:
                if coloring[neighbor] == c:
                    can_use = False
                    break
        if can_use:
            coloring[node] = c
            dfs(node+1,coloring)
            del coloring[node]
                
dfs(1,{})
print(count)
print(res)

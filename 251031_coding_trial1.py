math = ['m1','m2','m3']
sci = ['s1','s2','s3']
eng = ['e1']
group = [math,sci,eng]
res = []

def dfs(path):
    if len(path)==3:
        dfs_inside(path,0,[])
        return None 
    for i in range(len(group)):
        if group[i] not in path:
            path.append(group[i])
            dfs(path)
            path.pop()

def dfs_inside(block_order,layer,path2):
    if layer == 3:
        res.append(path2.copy())
        return None
        
    block = block_order[layer]
    
    def perm(temp):
        if len(temp)==len(block):
            dfs_inside(block_order,layer+1,path2+temp)
            return None 
        for x in block:
            if x not in temp:
                temp.append(x)
                perm(temp)
                temp.pop()
    perm([])
    
dfs([])

print(len(res))

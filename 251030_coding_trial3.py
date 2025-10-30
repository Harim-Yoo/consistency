nums = [1,2,3,4,5,6,7,8,9]
res = []

def dfs_2(start,group1):
    if len(group1)==3:
        remaining = list(set(nums)-set(group1))
        dfs_3(0,remaining,[],group1)
        return None 
    for i in range(start,len(nums)):
        group1.append(nums[i])
        dfs_2(i+1,group1)
        group1.pop()

def dfs_3(start,remaining,group2,group1):
    if len(group2)==3:
        group3 = list(set(nums)-set(group1)-set(group2))
        
        g3 = sorted(group3)
        g2 = sorted(group2)
        g1 = sorted(group1)
        
        partition = sorted([g1,g2,g3])
        if partition not in res:
            res.append(partition)
        return None
        
    for i in range(start,len(remaining)):
        group2.append(remaining[i])
        dfs_3(i+1,remaining,group2,group1)
        group2.pop()

dfs_2(0,[])
print(len(res))

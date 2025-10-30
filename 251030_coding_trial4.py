nums = [1,2,3,4,5,6]
res = []

def dfs_1(start,path):
    if len(path)==3:
        remaining = list(set(nums)-set(path))
        group1 = sorted(path)
        group2 = sorted(remaining)
        partition = [group1,group2]
        res.append(partition)
        return None 
    for i in range(start,len(nums)):
        path.append(nums[i])
        dfs_1(i+1,path)
        path.pop()

dfs_1(0,[])
print(len(res))

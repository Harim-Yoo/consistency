nums = [1,2,3,4,5]
res = []

   
def dfs(start,path):
    if len(path)==2:
        remaining_nums = [x for x in nums if x not in path]
        dfs_second(0,[],remaining_nums,sorted(path))
        return None 
    for i in range(start,len(nums)):
        path.append(nums[i])
        dfs(i+1,path)
        path.pop()

def dfs_second(start,new_path,remaining_nums,prev_path):
    if len(new_path)==2:
        remaining = [x for x in remaining_nums if x not in new_path]
        partition = sorted([sorted(prev_path),sorted(new_path),sorted(remaining)])
        if partition not in res:
            res.append(partition)
        return None
    for i in range(start,len(remaining_nums)):
        new_path.append(remaining_nums[i])
        dfs_second(i+1,new_path,remaining_nums,prev_path)
        new_path.pop()
        
dfs(0,[])
print(res)



    

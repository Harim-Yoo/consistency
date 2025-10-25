chars = [1,1,2,3,4]
chars.sort()
res = []
used = [False]*len(chars)

def dfs(path):
    if len(path) == len(chars):
        res.append(path.copy())
        return None
    for i in range(len(chars)):
        if used[i] == True :
            continue
        if i>0 and chars[i]==chars[i-1] and not used[i-1]:
            continue
        used[i] = True
        path.append(chars[i])
        dfs(path)
        path.pop()
        used[i] = False
dfs([])
print(len(res))

----------------------------------------------------------------------

nums = [1,1,1,3,4,5]
nums.sort()
res = []
used = [False]*len(nums)
def dfs(path):
    if len(path)==len(nums):
        res.append(path.copy())
        return None
    for i in range(0,len(nums)):
        if used[i] == True:
            continue
        if i>0 and nums[i] == nums[i-1] and used[i-1]==True:
            continue
        used[i]= True
        path.append(nums[i])
        dfs(path)
        path.pop()
        used[i]= False
dfs([])
print(len(res))

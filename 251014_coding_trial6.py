nums = [1,2,3,4,5]

def f(start, path):
    if len(path) == len(nums):
        return None
    for i in range(start,len(nums)):
        path.append(nums[i])
        if sum(path)==5:
            print(path)
        f(i+1,path)
        path.pop()

f(0,[])


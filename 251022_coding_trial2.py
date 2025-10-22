import math

target = 16000
nums = list(range(2,10))
res = []

def dfs(product, path):
    if product > target:
        return None
    if product == target:
        res.append(path.copy())
        return None
    for n in nums:
        new_product = product*n 
        path.append(n)
        dfs(new_product,path)
        path.pop()

dfs(1, [])

minimum = min(res,key=len)
print(minimum)

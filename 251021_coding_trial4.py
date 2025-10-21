nums = list(range(-5,6))
res = []
def dfs(start,path):
    if len(path)==3:
        if any(path[i]<0 for i in range(0,len(path))) and any(path[i]==0 for i in range(0,len(path))) and any(path[i]>0 for i in range(0,len(path))):
            res.append(path.copy())
        return None
    for i in range(start,len(nums)):
        path.append(nums[i])
        dfs(i+1,path)
        path.pop() 
dfs(0,[])

print(len(res))

----------------------------------------------------------------

import math 

N = 34*34*63*270
divs = []

def divisors(n):
    for i in range(1,int(math.isqrt(n))+1):
        if n % i == 0:
            divs.append(i)
            if i!= n//i:
                divs.append(n//i)
    return divs

divisors(N)

even = []
odd = []

for val in divs:
    if val%2==0:
        even.append(val) 
    else:
        odd.append(val)
        
value = sum(even) / sum(odd)
print(value)

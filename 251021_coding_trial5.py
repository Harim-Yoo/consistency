% Two distinct numbers are selected from the set $\{1,2,3,4,\dots,36,37\}$ so that the sum of the remaining $35$ numbers is the product of these two numbers. What is the difference of these two numbers?
$\textbf{(A) }5 \qquad \textbf{(B) }7 \qquad \textbf{(C) }8\qquad \textbf{(D) }9 \qquad \textbf{(E) }10$

import math 

nums = list(range(1,38))
res = []

def dfs(start,path):
    if len(path) == 2:
        if math.prod(path) ==  sum(nums)-sum(path):
            res.append(path.copy())
        return None
    for i in range(start,len(nums)):
        path.append(nums[i])
        dfs(i+1,path)
        path.pop()

dfs(0,[])
print(res)

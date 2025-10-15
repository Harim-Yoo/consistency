import math 
import sympy as sp

def product(path):
    p = 1 
    for prime, exp in path:
        p *= prime**exp
    return p

def dfs(prime,val,path):
    results = []
    if prime>val or product(path)>val:
        return results
    if product(path)==val:
        results.append(path.copy())
        return results
    
    exp = 0
    
    while (prime**exp) <= val:
        if exp>0:
            path.append((prime,exp))
        results += dfs(sp.nextprime(prime),val,path)
        if exp>0:
            path.pop()
        exp +=1
    
    return results
    
result = dfs(2,15,[])
print(result)

아...진짜 헷갈리네...

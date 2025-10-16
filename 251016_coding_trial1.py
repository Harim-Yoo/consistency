import math

def nextprime(n):
    def isprime(k):
        if k<2:
            return False
        for i in range(2,int(math.isqrt(k))+1):
            if k % i == 0:
                return False
        return True
    p = n + 1 
    while not isprime(p):
        p += 1 
    return p

def prime_factor(target_val):
    res = []
    
    def dfs(current_val,prime,path):
        if current_val == 1:
            res.append(path.copy())
            return
        if prime*prime > current_val:
            path.append((current_val,1))
            res.append(path)
            return
        
        exp = 0
        while current_val % prime == 0:
            exp +=1 
            current_val = current_val//prime 
        
        path.append((prime,exp))
        dfs(current_val,nextprime(prime),path)
    dfs(target_val,2,[])
    return res[0]

result = prime_factor(189745)

ans = []
for val in result:
    if val[1]!=0:
        ans.append(val)
print(ans)

import math

A = []

for y in range(0,100000000):
    n = math.isqrt(24*y+1)
    if n*n == 24*y+1:
        A.append(y)
        
print(A[1999])

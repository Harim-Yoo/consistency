import math

N = 1
for n in range(1,61):
    N *= math.factorial(n)

for k in range(1,61):
    num = N // math.factorial(k)
    x = math.isqrt(num)
    if x*x == num:
        print(k)

def f(n):
    if n == 1:
        return 1
    else:
        return n*f(n-1)
value = f(20)//(f(10)*f(10))

print(value)
count = 0 

for k in range(1,max(k for k in range(0,11) if 5**k<=value)+1):
    if value%(5**k)==0:
        count+=1

print(count)

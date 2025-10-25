def f(n):
    if n>2200:
        return n-2
    if 2200>=n>=0:
        return f(f(n+5))

print(f(2020))

def f(n):
    if n%2==0:
        return n-1
    else:
        return n**2-1

solution_set = []        
for n in range(-1000,1000):
    if f(f(n))==8:
        solution_set.append(n)

print(sum(solution_set))

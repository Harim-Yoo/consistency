#Purple Comet Problem 22 Find the number of functions f that map the set {1,2,3,4} into itself such that the rnage of the function f(x) equals that of f(f(x)).

from itertools import product

count = 0
values = [1,2,3,4]

for a,b,c,d in product(values,repeat = 4):
    f_map = (a,b,c,d)
    f_range = set(f_map)
    ff_range = set()
    def g(f_map,n):
        return f_map[n-1]
    for i in range(1,5):
        y = g(f_map,i)
        z = g(f_map,y)
        ff_range.add(z)
    if ff_range == f_range:
        count+=1 
print(count)

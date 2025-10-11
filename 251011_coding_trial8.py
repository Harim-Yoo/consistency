# If x and y are positive integers less than 100 such that x2 - y2 = 343, then (x,y) =

from itertools import product

solution = []
numbers = range(1, 101)

for (x,y) in product(numbers,repeat=2):
    if (x-y)*(x+y) == 343:
        solution.append((x,y))

print(solution)

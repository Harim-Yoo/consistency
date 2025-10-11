# Problem : The number of pairs of positive integers (x,y) which satisfy 2x + 3y = 515 is ?

#1st Attempt

from itertools import product

solution = []
numbers = range(1,int(float(515//2)))
for a in numbers:
  for b in numberes: #This looks like bashing
    if 2*a+3*b == 515:
      solution.append((a,b))
            
print(len(solution))

#2nd Attempt

from itertools import product

solution = []
numbers = range(1,int(float(515//2)))
for (a,b) in product(numbers,repeat=2): #itertools.product works fine.
    if 2*a+3*b == 515:
        solution.append((a,b))
            
print(len(solution))

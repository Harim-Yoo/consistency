#bruteforcing combination
user_list=[]
for a in range(1,12):
    for b in range(1,12):
        for c in range(1,12):
            if a<b<c:
                user_list.append((a,b,c))

count = 0

for x in user_list:
    if (x[0]+x[1]+x[2])%3 == 0:
        count +=1

print(count)    
---------------------------------------------------------------------------
#There is some library tool I could use in Python. Never knew. 

from itertools import combinations

count_new = 0
numbers = range(1,12)

for a,b,c in combinations(numbers,3):
  if (a+b+c)%3==0:
    count_new +=1

print(count_new)

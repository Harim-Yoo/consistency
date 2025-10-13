#2017 Purple Comet Math Meet Problem 29
----------------------------------------------------------------------------------
from itertools import combinations

vals = [1,2,3,4,5,6,7,8,9,10,11,12,13]
count = 0

for a,b,c in combinations(vals,3):
    if a%2!=0 and b%2!=0 and c%2!=0:
        pass
    elif a%3!=0 and b%3!=0 and c%3!=0:
        pass
    elif a%5!=0 and b%5!=0 and c%5!=0:
        pass
    else:
        count+=1

print(count)
----------------------------------------------------------------------------------
from itertools import combinations

vals = list(range(1,14))
count = 0

for a,b,c in combinations(vals,3):
    has1 = (a%2==0) or (b%2==0) or (c%2==0)
    has2 = (a%3==0) or (b%3==0) or (c%3==0)
    has3 = (a%5==0) or (b%5==0) or (c%5==0)
    if has1==True and has2==True and has3==True:
        count += 1
print(count)

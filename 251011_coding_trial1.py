#2005 Lehigh Math Meet Problem 34

#bashing. Didn't know that it would take this slow.

from itertools import product
count = 0
numbs = range(1,4001)
for a,b,c in product(numbs,repeat=3):
  if a*b*c == 4000:
    count +=1

print(count)

#Fixed version, using a bit of math more. 

from itertools import product

count_2 = 0
numbs_2 = range(0,6)
for a_1,a_2,a_3 in product(numbs_2,repeat=3):
  if a_1+a_2+a_3 == 5:
    count_2 +=1

count_5 = 0
numbs_5 = range(0,4)
for b_1,b_2,b_3 in product(numbs_5,repeat=3):
  if b_1+b_2+b_3 == 3:
    count_5 +=1
count = count_2 * count_5

print(count)

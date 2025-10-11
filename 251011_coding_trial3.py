# WalkThrouh Counting and Probability Problem 5

from itertools import permutations

count = 0
seat = [1,2,3,4,5]

for p in permutations(seat):
    for i in range(0,5):
        if p[i] == i+1:
            break
    else:
        count +=1 

print(count)

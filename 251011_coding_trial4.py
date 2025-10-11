#Gemini suggested problem 

from itertools import permutations

count = 0
seat = [1,2,3,4]

for p in permutations(seat):
    for i in range(0,3):
        if (p[i],p[i+1]) in [(1,2),(2,1)]:
            break
        elif (p[i],p[i+1]) in [(3,4),(4,3)]:
            break
    else:
        count +=1
        
print(count)

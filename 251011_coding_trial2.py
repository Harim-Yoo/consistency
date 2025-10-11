#Walk Through Counting and Probability Problem 4

#bashing because I didn't know how to set up nicer tricks of counting

from itertools import permutations

count = 0
numbs = [2,3,4,5]

for p in permutations(numbs):
    if (p[0],p[1])==(2,4) or (p[0],p[1])==(4,2):
        pass
    elif (p[2],p[3])==(2,4) or (p[2],p[3])==(4,2):
        pass
    elif (p[1],p[2])==(2,4) or (p[1],p[2])==(4,2):
        pass
    else:
        count +=1 

print(count)

#Better Tools ()

from itertools import permutations

count = 0 
numbs = [2,3,4,5]

def is_even(n):
    if n%2==0:
      return True

for p in permutations(numbs):
    for i in range(0,3):
      if is_even(p[i])==True and is_even(p[i+1])==True:
        break
    else:
        count +=1

print(count)
  

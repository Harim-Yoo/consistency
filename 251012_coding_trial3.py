import math 

numbers = [0,1,2,3,4,5]

string = []
for a in numbers:
    for b in numbers:
        for c in numbers:
            for d in numbers:
                if a!= 0 and d%2==1:
                    n = a*216+b*36+c*6+d 
                    x = math.isqrt(n)
                    if x*x == n:
                        string.append(([a,b,c,d],x))
                    
print(string)

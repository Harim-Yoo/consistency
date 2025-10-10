#2016 Lehigh Math Meet Problem 8

answer=[]

for n in range(100,1000):
    a,b,c = map(int,str(n))
    if a!= b and b!=c and c!=a:
        ratio = (100*a+10*b+c)/(a+b+c)
        answer.append((ratio,n))

def minimum(n):
    minimum = n[0]
    for x in n:
        if x[0] < minimum[0]:
            minimum = x
    return minimum

m = minimum(answer)

print(m)

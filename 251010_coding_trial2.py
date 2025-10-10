#2022 AMC10B Problem 3 - Parity trial

count = 0

for x in range(100,1000):
    a,b,c = map(int,str(x))
    sum = a+b+c 
    if sum%2==0:
        count+=1

print(count)

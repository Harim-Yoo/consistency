#2022 AMC10B Problem 3

count = 0

for x in range(100,1000):
    a,b,c = map(int,str(x))
    if a%2==0 and b%2==0 and c%2 ==0:
        count +=1 
    elif a%2==0 and b%2==1 and c%2==1:
        count +=1 
    elif a%2==1 and b%2==0 and c%2==1:
        count +=1 
    elif a%2==1 and b%2==1 and c%2==0:
        count +=1 

print(count)

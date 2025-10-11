#How many three-digit whole numbers satisfy the property that the middle digit is the average of the first and the last digits?

count = 0
for n in range(100,1000):
    a,b,c = map(int,str(n))
    if b == (a+c)/2:
        count+=1 
print(count)

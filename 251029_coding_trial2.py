count = 0 

for i in range(1,2005):
    string = str(i)
    count += string.count('0')

print(count)

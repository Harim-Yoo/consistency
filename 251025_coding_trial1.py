res = []

for k in range(0,500):
    res.append(str(2*k+1))

count = []
for val in res:
    count.append(val.count('9'))

print(sum(count))

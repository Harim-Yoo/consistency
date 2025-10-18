count = 0

for i in range(0,2019):
  x = bin(i)[2:]
  y = x.count("1")
  z = x.count("0")
  if y>z:
    count+=1

print(count)

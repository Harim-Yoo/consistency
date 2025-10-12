string=[]

for a in range(1,100):
    for b in range(a+1,100):
        for c in range(b+1,100):
            d = max(c+1,a+b+c)
            if d >=100:
                continue
            e = max(d+1,b+c+d)
            if e>=100:
                continue
            string.append((a,b,c,d,e))
print(string[:2])

count = 0
for a in range(-5,11):
    for b in range(-5,11):
        for c in range(-5,11):
            if a<b<c:
                if a*b*c<=50:
                    print((a,b,c))
                    count+=1

print(count)

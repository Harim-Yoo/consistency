numbs = range(100,1000)
answer_list = []
for n in numbs:
    a,b,c = map(int,str(n))
    if a!= b and b!=c and c!=a:
        answer_list.append(((100*a+10*b+c)/(a+b+c),n))
    
print(min(answer_list))

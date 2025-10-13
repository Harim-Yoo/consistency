#2022 AMC10A Problem 8

given_set = [1,7,5,2,5]

soln_set = []

for x in range(1,30):
    for vals in given_set:
        if (20+x)/6 == vals or (20+x)/6 == x:
            soln_set.append(x)
            
distinct_vals = set(soln_set)
print(sum(distinct_vals))

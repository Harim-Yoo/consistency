def sequence(n):
    return "1"*n + "2" + "1"*n
    
user_list = []
for n in range(1,11):
    user_list.append(sequence(n))

print(user_list)

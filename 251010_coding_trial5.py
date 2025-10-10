def sequence(n):
    return "1"*n + "2" + "1"*n
    
user_list = []
for n in range(1,11):
    user_list.append(sequence(n))

# swtiching a given list into integer 
def remainder_to_int(digits, n):
  r = 0
  for d in digits:
      r = (r*10 + int(d)) % n
  return r

number_list = []
for n in user_list:
    number_list.append((remainder_to_int(n,3),remainder_to_int(n,11)))

print(number_list)

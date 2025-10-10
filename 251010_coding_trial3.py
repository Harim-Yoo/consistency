# swtiching a given list into integer 
def digits_to_int(digits):
    x = 0
    for d in digits:
        x = x*10 + int(d)
    return x 

print(digits_to_int([1,2,3]))

# finding the modular form
def remainder_to_int(digits, n):
  r = 0
  for d in digits:
      r = (r*10 + int(d)) % n
  return r

print(remainder_to_int([1,2,3],2))

string = []

for n in range(1,3000):
    if n%2 == 0 and n%3 ==0 and n%5 ==0 and n%7 == 0 :
        string.append(n)

primes = [2,3,5,7]

for nums in string:
    has_prime_digits = False
    
    temp = nums
    
    while temp>0:
        last_digit = temp % 10
        temp = temp // 10
        
        if last_digit in primes:
            has_prime_digits = True
            break
    
    if has_prime_digits == False:
        print(nums)
            



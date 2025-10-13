import sympy as sp 
x = sp.Symbol('x',real=True)
val = sp.expand((x+1)**2000,x)
string = str(val)
terms = string.split('+')
odd_coefficients_count = 0
for term in terms:
    if '*x' in term:
        coefficient_str = term.split('*')[0]
        coefficient = int(coefficient_str)
    else:
        if 'x' in term:
            coefficient = 1
        else:
            coefficient = int(term)
    if coefficient%2 == 1:
        odd_coefficients_count +=1
    else:
        pass

print(odd_coefficients_count)

연습:

import sympy as sp 

x = sp.Symbol('x',real=True)
val = sp.expand((x+2)**5,x)
coeff_string = str(val)
terms = coeff_string.split('+')
ans_list = []
for term in terms:
    term = term.strip()
    if '*x' in term:
        coefficient_str = term.split('*')[0]
        coefficient = int(coefficient_str)
    else:
        if 'x' in term:
            coefficient = 1 
        else:
            coefficient = int(term)
    ans_list.append(coefficient)

count = 0

for val in ans_list:
    if val%2==0:
        continue
    else:
        count+=1

print(ans_list)
print(count)

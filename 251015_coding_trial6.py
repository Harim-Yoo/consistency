import sympy as sp

a = 8**(1/3)
b = 81**(-1/4)

expr = a/b

result = sp.simplify(expr)
print(int(result))

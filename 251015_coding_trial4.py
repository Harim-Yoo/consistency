import sympy as sp 

a = sp.Symbol('a',real=True)
b = sp.Symbol('b',real=True)

relation = sp.Eq(2*a,3*b+5)
sol_a = sp.solve(relation,a)[0]

expr = 4**sol_a/8**b
result = sp.simplify(expr)
print(result)

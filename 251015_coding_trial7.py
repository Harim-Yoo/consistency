import sympy as sp

x = sp.Symbol('x',real=True)
y = sp.Symbol('y',real=True)

expr_1 = 2/x 
expr_2 = y/3
expr_3 = x/y

eqtn_1 = sp.Eq(expr_1,expr_2)
eqtn_2 = sp.Eq(expr_2,expr_3)
result = sp.solve([eqtn_1,eqtn_2],[x,y])

print(result)
